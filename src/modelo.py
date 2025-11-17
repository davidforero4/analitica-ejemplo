from sklearn.linear_model import LinearRegression
import numpy as np

def entrenar_modelo(df):
    """
    Entrena un modelo de regresión lineal con las columnas:
    - X: dia
    - y: ventas
    """
    X = df[["dia"]]      # características
    y = df["ventas"]     # variable objetivo

    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

def predecir_venta(df, dia):
    """
    Entrena el modelo con el DataFrame df y predice las ventas
    para el día que pasamos como parámetro.
    """
    modelo = entrenar_modelo(df)
    prediccion = modelo.predict([[dia]])[0]
    return float(prediccion)
