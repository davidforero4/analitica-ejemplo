import sys
from pathlib import Path

# Aseguramos que Python vea la carpeta src
sys.path.append("src")

from load_data import cargar_ventas
from estadisticas import calcular_estadisticas
from graficos import grafico_linea


def main():
    print("=== Proyecto: Analítica de Ventas ===")

    # 1. Cargar datos
    df = cargar_ventas("data/ventas.csv")
    print("Datos cargados:")
    print(df.head())

    # 2. Calcular estadísticas
    stats = calcular_estadisticas(df)
    print("\nEstadísticas básicas:")
    print(stats)

    # 3. Guardar estadísticas en reports
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    stats_path = reports_dir / "estadisticas_ventas.csv"
    stats.to_csv(stats_path)
    print(f"\nEstadísticas guardadas en: {stats_path}")

    # 4. Generar y guardar gráfico
    grafico_linea(df, save=True)


if __name__ == "__main__":
    main()