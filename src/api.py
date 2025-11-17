from fastapi import FastAPI, HTTPException

from .database import inicializar_bd, obtener_ventas_semana
from .estadisticas import calcular_estadisticas
from .modelo import predecir_venta


app = FastAPI(title="API de Ventas (ejemplo)")

@app.on_event("startup")
def on_startup():
    # Asegura que la base de datos exista al iniciar la API
    inicializar_bd()

@app.get("/")
def raiz():
    return {"mensaje": "API de ejemplo para analítica de ventas"}

@app.get("/ventas/{semana}")
def ventas_semana(semana: int):
    df = obtener_ventas_semana(semana)
    if df.empty:
        raise HTTPException(status_code=404, detail="Semana no encontrada")
    return df.to_dict(orient="records")

@app.get("/estadisticas/{semana}")
def estadisticas_semana(semana: int):
    df = obtener_ventas_semana(semana)
    if df.empty:
        raise HTTPException(status_code=404, detail="Semana no encontrada")
    stats = calcular_estadisticas(df[["ventas"]])
    return stats.to_dict()

@app.get("/predecir")
def predecir(dia: int, semana: int = 1):
    df = obtener_ventas_semana(semana)
    if df.empty:
        raise HTTPException(status_code=404, detail="Semana no encontrada")
    pred = predecir_venta(df, dia)
    return {
        "semana": semana,
        "dia": dia,
        "ventas_predichas": pred,
    }
