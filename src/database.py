import sqlite3
from pathlib import Path
import pandas as pd

# Carpeta raíz del proyecto (ANALITICA-EJEMPLO)
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpeta de datos
DATA_DIR = BASE_DIR / "data"

# Ruta completa a la base de datos
DB_PATH = DATA_DIR / "ventas.db"


def inicializar_bd():
    """
    Crea la base de datos y la tabla de ventas si no existen,
    y carga los datos de los CSV de semana 1 y 2.
    """

    # Aseguramos que la carpeta data exista
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Si la BD ya existe, no hacemos nada
    if DB_PATH.exists():
        return

    # Conexión a la base de datos (se crea si no existe)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear tabla
    cur.execute("""
        CREATE TABLE ventas (
            semana INTEGER,
            dia INTEGER,
            ventas REAL
        )
    """)

    # Cargar CSV semana 1
    df1 = pd.read_csv(DATA_DIR / "ventas.csv")
    df1["semana"] = 1

    # Cargar CSV semana 2
    df2 = pd.read_csv(DATA_DIR / "ventas_semana2.csv")
    df2["semana"] = 2

    # Unir y guardar en la BD
    df = pd.concat([df1, df2], ignore_index=True)
    df[["semana", "dia", "ventas"]].to_sql(
        "ventas",
        conn,
        if_exists="append",
        index=False
    )

    conn.commit()
    conn.close()


def obtener_ventas_semana(semana: int) -> pd.DataFrame:
    """
    Devuelve un DataFrame con las ventas de la semana indicada.
    """
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT dia, ventas FROM ventas WHERE semana = ? ORDER BY dia"
    df = pd.read_sql_query(query, conn, params=(semana,))
    conn.close()
    return df
