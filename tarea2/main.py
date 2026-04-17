"""
Código para calcular frecuencias, probabilidades, momentos y varianza de datos.
Alejandra Coeto - A01285221
"""

def calcular_frecuencias(nums) -> dict:
    """Calcula la frecuencia de cada número en la lista."""
    frecuencias = dict()

    for num in nums:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    
    return frecuencias

def calcular_probabilidades(nums, frecuencias) -> list:
    """Calcula la probabilidad de cada número basado en su frecuencia."""
    probabilidades = []

    print("Valor \tFrecuencia \tProbabilidad")
    for num, freq in frecuencias.items():
        prob = freq / len(nums)
        probabilidades.append(prob)
        print(f"{num} \t{freq} \t\t{prob:.2f}")

    return probabilidades

def calcular_momentos(frecuencias, probabilidades) -> tuple:
    """Calcula los momentos 1, 2, 3 y 4 de los datos."""
    momento_1 = 0
    momento_2 = 0
    momento_3 = 0
    momento_4 = 0

    for i, (num, _) in enumerate(frecuencias.items()):
        prob = probabilidades[i]
        momento_1 += num * prob
        momento_2 += (num ** 2) * prob
        momento_3 += (num ** 3) * prob
        momento_4 += (num ** 4) * prob

    return momento_1, momento_2, momento_3, momento_4


def calcular_varianza(momento_1, momento_2) -> float:
    """Calcula la varianza usando los momentos 1 y 2."""
    return momento_2 - (momento_1 ** 2)

def descrptivos_estadisticos(nums) -> None:
    """Calcula y muestra los descriptivos estadísticos de una lista de números."""
    print("------------------------------------")
    print(f"Datos: {nums}")
    print("--- Frecuencias y probabilidades ---")
    frecuencias = calcular_frecuencias(nums)
    probabilidades = calcular_probabilidades(nums, frecuencias)

    print("\n--- Momentos ---")
    momento_1, momento_2, momento_3, momento_4 = calcular_momentos(frecuencias, probabilidades)
    print(f"Momento 1: {momento_1:<10.2f}")
    print(f"Momento 2: {momento_2:<10.2f}")
    print(f"Momento 3: {momento_3:<10.2f}")
    print(f"Momento 4: {momento_4:<10.2f}")

    varianza = calcular_varianza(momento_1, momento_2)
    print(f"Varianza calculada: {varianza:.2f}")
    print()

def main():
    # Primer conjunto de datos
    X=[1,1,2,1,3,4,2,1,3,2]
    descrptivos_estadisticos(X)

    # Segundo conjunto de datos
    Y=[4,2,2,2,1,2,1,2,4,3,3,3,1,3,3,4,3,3,1,4,5,5,2,1,5,1,4,2,5,3,2,5,3,1,5,3,2,3,2,4,3,3,2,3,1,3,1,3,5,2,1,1,5,5,5,2,5,2,1,4,5,3,3,1,1,3,2,1,4,1,4,3,3,3,5,4,1,5,4,1,2,2,4,1,3,1,2,3,1,3,4,2,3,5,4,1,3,1,3,4]
    descrptivos_estadisticos(Y)

if __name__ == "__main__":
    main()