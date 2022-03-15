"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição

Exercício 6:

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
"""

n = int(input('Digite o numero de termos: '))
H = 1

for i in range(2, n+1):
    H = H + (1 / i)
    
print(f'\nO valor aproximado de H com {n} termos é: {H:.4f}')