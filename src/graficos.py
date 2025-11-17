import matplotlib.pyplot as plt
from pathlib import Path

def grafico_linea(df, save=False, path="../reports/figures/ventas.png"):
    plt.plot(df["dia"], df["ventas"])
    plt.xlabel("Día")
    plt.ylabel("Ventas")
    plt.title("Ventas por día")

    if save:
        ruta = Path(path)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(ruta)
        print(f"Gráfico guardado en: {ruta}")

    plt.show()