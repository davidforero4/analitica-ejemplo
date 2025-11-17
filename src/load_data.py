import pandas as pd

def cargar_ventas(path="../data/ventas.csv"):
    df = pd.read_csv(path)
    return df
