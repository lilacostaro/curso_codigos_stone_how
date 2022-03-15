"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição

Exercício 2:

Escreva um programa que exiba uma tabela de conversão de temperatura para graus Celsius e graus Fahrenheit. 
A tabela deve incluir linhas para todas as temperaturas entre 0 e 100 graus Celsius que são múltiplos de 10 graus Celsius. 
Dê um título apropriado para cada coluna. 
A fórmula para converter entre graus Celsius e graus Fahrenheit podem ser encontrados na Internet (faz parte do exercício pesquisar!)
"""
import pandas as pd

c = []
f = []

for temp in range(0, 101, 10):
    fah = (temp * (9 / 5)) + 32
    c.append(temp)
    f.append(fah)
    
table = list(zip(c, f))
df = pd.DataFrame(table, columns = ['°C','°F'])

print('\nConversão de °C para °F\n')
print(df)


