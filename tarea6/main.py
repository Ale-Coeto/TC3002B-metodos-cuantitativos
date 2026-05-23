"""
Código para resolver problemas de distribuciones Uniforme y Exponencial.
Alejandra Coeto - A01285221
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def problema_cafeteria_caja():
	print("--- Problema 1: Tiempo de Atención en Caja ---")
	a = 2
	b = 8
	
	# a)
	prob_3_6 = (6 - 3) / (b - a)
	print(f"a) P(3 - 6) = {prob_3_6:.4f}")
	
	# b) Tiempo promedio esperado
	media = (a + b) / 2
	print(f"b) E[X] = {media:.4f} minutos")
	
	# c) Varianza
	varianza = (b - a) ** 2 / 12
	print(f"c) Var(X) = {varianza:.4f}")
	

def problema_impresion():
	print("--- Problema 3: Tiempo de Espera Entre Llegadas ---")
	tasa_hora = 4
	
	# a) Tasa lambda
	lambda_hora = tasa_hora
	lambda_minuto = tasa_hora / 60
	print(f"a) lambda = {lambda_hora} estudiantes/hora")
	
	# b) P(X < 10 minutos)
	t1 = 10
	prob_menor_10 = 1 - math.exp(-lambda_minuto * t1)
	print(f"b) P(X < 10 min) = {prob_menor_10:.4f}")
	
	# c) P(X > 20 minutos)
	t2 = 20
	prob_mayor_20 = math.exp(-lambda_minuto * t2)
	print(f"c) P(X > 20 min) = {prob_mayor_20:.4f}")


def problema_variable_aleatoria():
	print("--- Problema 1: Variable Aleatoria Discreta ---")
	
	probabilidades = [0.10, 0.35, 0.30, 0.15, 0.10]
	valores_x = [0, 1, 2, 3, 4]
	intervalos = [(0, 0.10), (0.10, 0.45), (0.45, 0.75), (0.75, 0.90), (0.90, 1.0)]
	
    # Números aleatorios entre 0 y 1
	r = np.random.uniform(0, 1, 1000)
	
    # Asignar a intervalos
	x_simulado = []
	for numero in r:
		for i, (a, b) in enumerate(intervalos):
			if a < numero <= b:
				x_simulado.append(valores_x[i])
				break
	
    # Frecuencias absolutas y relativas
	frecuencias_abs = [x_simulado.count(x) for x in valores_x]
	frecuencias_rel = [freq / 1000 for freq in frecuencias_abs]
	
	print("Valor X | Freq. Abs | Freq. Rel | Prob. Teórica")
	for i, x in enumerate(valores_x):
		print(f"   {x}   |    {frecuencias_abs[i]:3d}    |  {frecuencias_rel[i]:.4f}   |    {probabilidades[i]:.4f}")
	print()
	
    # Gráfica
	plt.figure(figsize=(10, 6))
	x_pos = np.arange(len(valores_x))
	width = 0.35
	
	plt.bar(x_pos - width/2, frecuencias_rel, width, label='Simulado', alpha=0.8)
	plt.bar(x_pos + width/2, probabilidades, width, label='Teórico', alpha=0.8)
	
	plt.xlabel('Valor de X')
	plt.ylabel('Probabilidad')
	plt.title('Frecuencias Simuladas vs Probabilidades Teóricas')
	plt.xticks(x_pos, valores_x)
	plt.legend()
	plt.grid(axis='y', alpha=0.3)
	plt.tight_layout()
	plt.savefig('distribucion_variable_aleatoria.png', dpi=100)
	plt.show()


def problema_poisson():
	print("--- Problema 3: Simulación de Poisson ---")
	
	valores_x = [0, 1, 2, 3, 4, 5]
	probabilidades = [0.0498, 0.1494, 0.2240, 0.2240, 0.1680, 0.1008]
	acumuladas = [0.0498, 0.1992, 0.4232, 0.6472, 0.8152, 0.9160]
	
    # Números aleatorios entre 0 y 1
	r = np.random.uniform(0, 1, 1000)
	
    # Asignar con acumuladas
	x_simulado = []
	for numero in r:
		for i, acum in enumerate(acumuladas):
			if numero <= acum:
				x_simulado.append(valores_x[i])
				break
	
    # Frecuencias absolutas y relativas
	frecuencias_abs = [x_simulado.count(x) for x in valores_x]
	frecuencias_rel = [freq / 1000 for freq in frecuencias_abs]
	
	media_simulada = sum(x * freq for x, freq in zip(valores_x, frecuencias_rel))
	lambda_teorico = 3
	
	print(f"Media simulada: {media_simulada:.4f}")
	print(f"Lambda teórico: {lambda_teorico:.4f}\n")
	
	print("Valor X | Freq. Abs | Freq. Rel | Prob. Teórica")
	for i, x in enumerate(valores_x):
		print(f"   {x}   |    {frecuencias_abs[i]:3d}    |  {frecuencias_rel[i]:.4f}   |    {probabilidades[i]:.4f}")
	print()
	
    # Gráfica
	plt.figure(figsize=(10, 6))
	x_pos = np.arange(len(valores_x))
	width = 0.35
	
	plt.bar(x_pos - width/2, frecuencias_rel, width, label='Simulado', alpha=0.8)
	plt.bar(x_pos + width/2, probabilidades, width, label='Teórico', alpha=0.8)
	
	plt.xlabel('Número de estudiantes (X)')
	plt.ylabel('Probabilidad')
	plt.title('Frecuencias Simuladas vs Distribución de Poisson (lambda=3)')
	plt.xticks(x_pos, valores_x)
	plt.legend()
	plt.grid(axis='y', alpha=0.3)
	plt.tight_layout()
	plt.savefig('distribucion_poisson.png', dpi=100)
	plt.show()


def main():
	print("=== Distribución Uniforme ===\n")
	problema_cafeteria_caja()
	
	print("\n=== Distribución Exponencial ===\n")
	problema_impresion()
	
	print("\n=== Variable Aleatoria Discreta ===\n")
	problema_variable_aleatoria()
	
	print("\n=== Distribución de Poisson ===\n")
	problema_poisson()


if __name__ == "__main__":
	main()
