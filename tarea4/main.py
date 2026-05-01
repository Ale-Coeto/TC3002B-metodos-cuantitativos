"""
Código para resolver problemas de distribución Gemoétrica y de Poisson.
Alejandra Coeto - A01285221
"""

import math

def prob_poisson(lambd, k):
	"""
	Calcula P(X = k) para una variable aleatoria Poisson con parámetro lambd.
	"""
	return (math.exp(-lambd) * (lambd ** k)) / math.factorial(k)


def prob_geometrica_primera_en_n(p, n):
	"""
	Calcula P(X = n) para una variable geométrica (primer éxito en el intento n).
	"""
	q = 1 - p
	return (q ** (n - 1)) * p

def problema_piezas_defectuosas():
	print("--- Problema 2: Inspección de Piezas Defectuosas ---")
	p = 0.10
	q = 1 - p

	# a) Probabilidad de inspeccionar 4 o menos piezas
	prob_a = 1 - (q ** 4)
	print(f"A) P(X <= 4): {prob_a:.4f}")

	# b) Número esperado de piezas inspeccionadas
	esperado = 1 / p
	print(f"B) E[X]: {esperado:.4f}\n")


def problema_desviacion_excesiva():
	print("--- Problema 4: Desviación Excesiva en Dispositivos ---")
	p = 0.05
	n = 6

	probabilidad = prob_geometrica_primera_en_n(p, n)
	print(f"P(X = 6): {probabilidad:.6f}\n")

def problema_hojalata():
	print("--- Problema 2: Inspección de Hojalata ---")
	tasa_por_minuto = 0.2

	# A) Una imperfección en 3 minutos
	lambda_a = tasa_por_minuto * 3
	prob_a = prob_poisson(lambda_a, 1)
	print(f"A) P(X = 1) en 3 min: {prob_a:.4f}")

	# B) Al menos dos imperfecciones en 5 minutos
	lambda_b = tasa_por_minuto * 5
	prob_b = 1 - (prob_poisson(lambda_b, 0) + prob_poisson(lambda_b, 1))
	print(f"B) P(X >= 2) en 5 min: {prob_b:.4f}")

	# C) Cuando más una imperfección en 15 minutos
	lambda_c = tasa_por_minuto * 15
	prob_c = prob_poisson(lambda_c, 0) + prob_poisson(lambda_c, 1)
	print(f"C) P(X <= 1) en 15 min: {prob_c:.4f}\n")


def problema_componentes():
	print("--- Problema 4: Fallos de Componentes Electrónicos ---")
	media_100_horas = 8
	tasa_por_hora = media_100_horas / 100

	# A) Que falle un componente en 25 horas
	lambda_a = tasa_por_hora * 25
	prob_a = prob_poisson(lambda_a, 1)
	print(f"A) P(X = 1) en 25 h: {prob_a:.4f}")

	# B) Que fallen no más de dos componentes en 50 horas
	lambda_b = tasa_por_hora * 50
	prob_b = sum(prob_poisson(lambda_b, k) for k in range(3))
	print(f"B) P(X <= 2) en 50 h: {prob_b:.4f}")

	# C) Que fallen por lo menos diez componentes en 125 horas
	lambda_c = tasa_por_hora * 125
	prob_c = 1 - sum(prob_poisson(lambda_c, k) for k in range(10))
	print(f"C) P(X >= 10) en 125 h: {prob_c:.4f}\n")
	
def main():
	print("=== Distribuciones Geométricas ===\n")
	problema_piezas_defectuosas()
	problema_desviacion_excesiva()
	print("=== Distribuciones de Poisson ===\n")
	problema_hojalata()
	problema_componentes()


if __name__ == "__main__":
	main()
