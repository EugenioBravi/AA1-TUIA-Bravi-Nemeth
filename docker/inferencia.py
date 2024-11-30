import pandas as pd
import numpy as np
import joblib
import sys

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
imputer = joblib.load("imputer.pkl")

def infer(data_path):
    try:
        data = pd.read_csv(data_path)
    
        data_imputed = imputer.transform(data)
        data_scaled = scaler.transform(data_imputed)
        
        predictions = model.predict(data_scaled)
        predictions_proba = model.predict_proba(data_scaled)
        
        result = data.copy()
        result['Prediction'] = predictions
        result['RainTomorrow_Probability'] = predictions_proba[:, 1]
        
        result.to_csv("predictions.csv", index=False)
        print("Predicciones guardadas en predictions.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python inferencia.py <ruta_datos>")
    else:
        infer(sys.argv[1])
