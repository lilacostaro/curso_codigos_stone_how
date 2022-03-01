"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: tipos numéricos
Diversão do carnaval \o/

Exercício 1:

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;

Dica!
Para calcular o log10, utilize a função log10 do módulo math conforme exemplo abaixo
>>> from math import log10
>>> log10(100)
2.0
"""
# importando o modulo
from math import log10

# Recebendo o input do usuario
num_1 = int(input('Digite um numero inteiro: '))
num_2 = int(input('Digite outro numero inteiro: '))

# Imprimindo os resultados
print(f'\nA soma de {num_1} e {num_2} é: {num_1 + num_2}')
print(f'\nA diferença entre {num_2} e {num_1} é: {num_2 - num_1}')
print(f'\nO produto dos numeros {num_1} e {num_2} é: {num_1 * num_2}')
print(f'\nO quociente da divisão de {num_1} por {num_2} é: {num_1 // num_2}')
print(f'\nO resto da divisão de {num_1} por {num_2} é: {num_1 % num_2}')
print(f'\nO log10 de {num_1} é: {log10(num_1)}')
print(f'\nA valor de {num_1} elevado a {num_2} é: {num_1 ** num_2}')

