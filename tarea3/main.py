"""
Código para resolver problemas de distribuciones de Bernoulli y Binomial.
Alejandra Coeto - A01285221
"""

import math

def problema_barniz():
    """
    Resuelve el problema de la aplicación de barniz en una superficie cerámica.
    """
    print("--- Problema 2: Barniz en Cerámica ---")
    # Probabilidad de que ocurra un defecto (decoloración, agrietamiento o ambos)
    prob_defecto = 0.05

    # a. Probabilidad de éxito (que no le pase nada a la pieza)
    p = 1 - prob_defecto
    print(f"P(X = 1) = {p:.2f}\n")

    # b. Valor esperado de x
    valor_esperado = p
    print(f"E[X] = p = {valor_esperado:.2f}\n")

    # c. Varianza de x
    varianza = p * (1 - p)
    print(f"Var(x) = {varianza:.4f}\n")

def problema_dados():
    """
    Resuelve el problema de lanzar dos dados de seis caras.
    """
    print("--- Problema 4: Lanzamiento de Dos Dados ---")
    total_outcomes = 36

    # Variable 1: Que ambos dados caigan en el mismo número
    print("Variable 1: Ambos dados caen en el mismo número.")
    successful_outcomes_1 = 6
    p1 = successful_outcomes_1 / total_outcomes
    valor_esperado_1 = p1
    varianza_1 = p1 * (1 - p1)
    print(f"E[X] = {valor_esperado_1:.4f}")
    print(f"Var(X) = {varianza_1:.4f}\n")

    # Variable 2: Que ambos dados caigan en 1
    print("Variable 2: Ambos dados caen en 1.")
    successful_outcomes_2 = 1
    p2 = successful_outcomes_2 / total_outcomes
    valor_esperado_2 = p2
    varianza_2 = p2 * (1 - p2)
    print(f"E[X] = {valor_esperado_2:.4f}")
    print(f"Var(X) = {varianza_2:.4f}\n")


def problema_farmacia():
    """
    Resuelve el problema de probabilidad de los estudiantes de farmacia.
    """
    print("--- Problema 2: Estudiantes de Farmacia ---")
    n = 7
    p = 0.03
    q = 1 - p

    # a. Ninguno
    prob_ninguno = math.comb(n, 0) * (p**0) * (q**7)
    print(f"a. Probabilidad de que ninguno acabe: {prob_ninguno:.4f}")

    # b. Todos
    prob_todos = math.comb(n, 7) * (p**7) * (q**0)
    print(f"b. Probabilidad de que todos acaben: {prob_todos:.4e}")

    # c. Al menos dos acaben la carrera
    prob_uno = math.comb(n, 1) * (p**1) * (q**6)
    prob_al_menos_dos = 1 - prob_ninguno - prob_uno
    print(f"c. Probabilidad de que al menos dos acaben: {prob_al_menos_dos:.4f}")

    # d. Media y desviación estándar
    media = n * p
    varianza = n * p * q
    desviacion_estandar = math.sqrt(varianza)
    print(f"d. Media: {media:.4f}")
    print(f"   Desviación Estándar: {desviacion_estandar:.4f}\n")

def problema_familia():
    """
    Calcula la probabilidad de que una familia con cuatro hijos tenga tres niños.
    """
    print("--- Problema 4: Familia con Cuatro Hijos ---")
    n = 4
    k = 3
    p = 0.5
    q = 1 - p

    probabilidad = math.comb(n, k) * (p**k) * (q**(n-k))
    print(f"La probabilidad de que 3 de 4 hijos sean niños es: {probabilidad:.4f}\n")


def main():
    # Bernoulli
    print("=== Distribución de Bernoulli ===\n")
    problema_barniz()
    problema_dados()

    # Binomial
    print("=== Distribución Binomial ===\n")
    problema_farmacia()
    problema_familia()
    _ = ""

if __name__ == "__main__":
    main()
