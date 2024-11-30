import pandas as pd
import numpy as np
import joblib
import sys

def infer(data_path):
    try:
        data = pd.read_csv(data_path)
        print(f"Datos cargados desde {data_path}")
        print(f"Columnas: {data.columns}")

        # make a new result dataframe to return a predictions.csv as output
        result = pd.DataFrame()
        result["ID"] = data["MaxTemp"]

        result.to_csv("/output/predicciones.csv", index=False)
        print("Predicciones guardadas en predicciones.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    infer("/output/weather_docker.csv")
