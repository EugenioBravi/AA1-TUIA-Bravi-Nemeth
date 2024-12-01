import pandas as pd
import numpy as np
import keras

def infer(data_path):
    try:
        # Leemos el modelo
        modelo_nn = keras.models.load_model("./models/modelo_nn.h5")
        # Leemos el archivo a predecir
        data = pd.read_csv(data_path)
        medias_mensuales = pd.read_csv('./models/medias_mensuales.csv')
        modas_mensuales = pd.read_csv('./models/modas_mensuales.csv')

        # Tratamos las fechas
        data['Date'] = pd.to_datetime(data['Date'])
        data['Month'] = data['Date'].dt.month
        data.drop('Date', axis=1, inplace=True)

        # Tratamos valores faltantes
        for index, row in data.iterrows():
            month = row['Month'] - 1  
            for column in medias_mensuales.columns:
                if pd.isna(data.loc[index, column]):  
                    data.loc[index, column] = medias_mensuales.loc[month, column]

        for index, row in data.iterrows():
            month = row['Month'] - 1  
            for column in modas_mensuales.columns:
                if pd.isna(data.loc[index, column]): 
                    data.loc[index, column] = modas_mensuales.loc[month, column]
        
        # Tratamos RainToday
        data['RainToday'] = data['RainToday'].map({'Yes': 1, 'No': 0})

        #Tratamos las ciudades
        location_coordenadas = {
            'Wollongong': [-34.43305,150.88305 ],
            'Ballarat': [-37.56622, 143.84957],
            'MountGinini': [-35.28346, 149.12807],
            'Hobart': [-42.88333,147.31666 ],
            'Williamtown': [-32.80899, 151.83899],
            'Adelaide': [-34.92866, 138.59863],
            'Sale': [-33.86785, 151.20732],
            'Penrith': [-33.75111, 150.69416],
            'Woomera': [-31.16563, 136.81926],
            'SalmonGums': [-32.98207, 121.64416]
        }
        data['Latitud'] = data['Location'].map(lambda loc: location_coordenadas[loc][0])
        data['Longitud'] = data['Location'].map(lambda loc: location_coordenadas[loc][1])
        data = data.drop(columns=['Location'])

        #Tratamos los puntos cardinales
        angulos = {
            'N': 0,
            'NNE': 22.5,
            'NE': 45,
            'ENE': 67.5,
            'E': 90,
            'ESE': 112.5,
            'SE': 135,
            'SSE': 157.5,
            'S': 180,
            'SSW': 202.5,
            'SW': 225,
            'WSW': 247.5,
            'W': 270,
            'WNW': 292.5,
            'NW': 315,
            'NNW': 337.5
        }
        for column in ['WindGustDir','WindDir9am','WindDir3pm']:
            data[column] = data[column].map(angulos)

        #Hacemos la prediccion
        y_pred_nn = modelo_nn.predict(data)
        y_pred_nn = np.where(y_pred_nn >= 0.5, 1, 0)
        
        #Creamos el dataframe con los resultados
        result = pd.DataFrame({'llueve': y_pred_nn.flatten()})
        result['llueve'] = result['llueve'].map({1: 'Yes', 0: 'No'})

        result.to_csv("/output/predicciones.csv", index=False)
        print("Predicciones guardadas en predicciones.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    infer("/output/weather_docker.csv")
