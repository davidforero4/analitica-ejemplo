import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_BASE_URL = "http://127.0.0.1:8000"


def obtener_ventas(semana: int) -> pd.DataFrame:
    """
    Llama al endpoint /ventas/{semana} y devuelve un DataFrame.
    """
    url = f"{API_BASE_URL}/ventas/{semana}"
    resp = requests.get(url)
    resp.raise_for_status()  # lanza error si algo falla
    data = resp.json()       # lista de diccionarios
    df = pd.DataFrame(data)
    return df


def predecir_ventas(semana: int, dia: int) -> float:
    """
    Llama al endpoint /predecir?semana=...&dia=...
    y devuelve la predicción numérica.
    """
    url = f"{API_BASE_URL}/predecir"
    params = {"semana": semana, "dia": dia}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["ventas_predichas"]


def main():
    st.title("Dashboard de Ventas usando la API")
    st.write("Este dashboard consume la API FastAPI que creaste para hacer análisis y predicciones.")

    # Seleccionar semana
    semana = st.selectbox("Selecciona la semana:", [1, 2])

    # Obtener datos desde la API
    try:
        df = obtener_ventas(semana)
    except Exception as e:
        st.error(f"No se pudieron obtener los datos desde la API: {e}")
        return

    st.subheader(f"Datos de ventas - Semana {semana}")
    st.dataframe(df)

    # Gráfico de línea
    st.subheader("Gráfico de ventas")
    fig, ax = plt.subplots()
    ax.plot(df["dia"], df["ventas"], marker="o")
    ax.set_xlabel("Día")
    ax.set_ylabel("Ventas")
    ax.set_title(f"Ventas por día - Semana {semana}")
    st.pyplot(fig)

    # Predicción
    st.subheader("Predicción de ventas")
    dia = st.slider("Selecciona el día para predecir", min_value=1, max_value=14, value=7)

    try:
        pred = predecir_ventas(semana, dia)
        st.write(f"Ventas predichas para la semana {semana}, día {dia}: **{pred:.2f}**")
    except Exception as e:
        st.error(f"No se pudo obtener la predicción desde la API: {e}")


if __name__ == "__main__":
    main()
