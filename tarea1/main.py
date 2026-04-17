"""
Se grafican tres histogramas de vectores con diferentes medias y varianzas para observar cómo afectan la forma y la distribución.
Alejandra Coeto - A01285221
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # Para reproducibilidad

def crear_vector(media: float, varianza: float, tamaño: int) -> np.ndarray:
    """Crea un vector de números aleatorios con una distribución normal dada su media y varianza."""
    return np.random.normal(loc=media, scale=np.sqrt(varianza), size=tamaño)

def graficar_histograma(vector: np.ndarray, titulo: str):
    """Grafica un histograma del vector dado y muestra su media y varianza en el título."""
    plt.figure()
    plt.hist(vector, bins=30)
    plt.title(titulo)

def graficar_tres_histogramas(v1, v2, v3, bins=30):
    """Grafica tres histogramas combinados con diferentes vectores."""
    plt.figure()
    plt.hist(v1, bins=bins, alpha=0.5, label="V1: media=0, var=1")
    plt.hist(v2, bins=bins, alpha=0.5, label="V2: media=20, var=1")
    plt.hist(v3, bins=bins, alpha=0.5, label="V3: media=0, var=20")
    plt.legend()
    plt.title("Histogramas combinados")
    
def main():
    # Vector con media = 0 y varianza = 1
    data1 = crear_vector(0, 1, 500)
    graficar_histograma(data1, "Vector con media = 0 y varianza = 1")
    print(np.sqrt(1))

    # Vector con media = 20 y varianza = 1
    data2 = crear_vector(20, 1, 500)
    graficar_histograma(data2, "Vector con media = 20 y varianza = 1")

    # Vector con media = 0 y varianza = 20
    data3 = crear_vector(0, 20, 500)
    graficar_histograma(data3, "Vector con media = 0 y varianza = 20")

    # Graficar los 3 histogramas juntos
    graficar_tres_histogramas(data1, data2, data3)

    plt.show()
    
if __name__ == "__main__":
    main()
