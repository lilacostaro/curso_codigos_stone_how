"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição

Exercício 4 (desafio):

Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):
    
Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!
"""
pi = 3

for i in range(1, 15):
    f = i * 2
    valor = (4 / ((f) * (f + 1) * (f + 2)))
    if i % 2 == 0:
        pi -= valor
    else:
        pi += valor
    
print(f'\nO valor aproximado de pi é {pi}')


