"""
Código para resolver problemas de distribuciones Normal y Exponencial.
Alejandra Coeto - A01285221
"""

import math


def problema_bomba():
	print("--- Problema 2: Bomba en una Línea ---")
	longitud_linea = 1000
	distancia_destruccion = 75

	# Probabilidad de destruir el blanco
	longitud_favorable = 2 * distancia_destruccion
	probabilidad = longitud_favorable / longitud_linea
	print(f"P(Destruir el blanco) = {probabilidad:.4f}\n")


def problema_amigos():
	print("--- Problema 4: Encuentro en Parada de Camión ---")
	intervalo_total = 60
	espera_maxima = 10

	# Probabilidad de que se encuentren
	intervalo_favorable = 2 * espera_maxima
	probabilidad = intervalo_favorable / intervalo_total
	print(f"P(Se encuentren) = {probabilidad:.4f}\n")


def problema_bateria():
	print("--- Problema 2: Duración de Batería ---")
	media = 500
	t = 600

	# Probabilidad de que funcione por más de 600 horas
	probabilidad = math.exp(-t / media)
	print(f"P(X > 600) = {probabilidad:.4f}\n")


def problema_cafeteria():
	print("--- Problema 4: Atención en Cafetería ---")
	media = 4

	# Valor esperado solicitado
	valor_esperado = 1 / media
	print(f"E[X] = {valor_esperado:.4f}\n")


def main():
	# Normal
	print("=== Distribución Normal ===\n")
	problema_bomba()
	problema_amigos()

	# Exponencial
	print("=== Distribución Exponencial ===\n")
	problema_bateria()
	problema_cafeteria()
	_ = ""


if __name__ == "__main__":
	main()
