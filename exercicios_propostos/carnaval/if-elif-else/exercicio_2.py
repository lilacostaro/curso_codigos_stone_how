"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 2:

Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""
# Recebendo o input do usuario
num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))

# Condição
if (num_1 % num_2) == 0:
    print(f'O número {num_1} é divisivel por {num_2}')
else:
    print(f'O número {num_1} não é divisivel por {num_2}')