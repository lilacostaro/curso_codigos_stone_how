"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 1:

Escreva um programa que diga se um número dado pelo usuário é par ou ímpar
"""
# Recebendo numero do usuario
num = int(input('Digite um número interio: '))

# Dedinindo a condição
if (num % 2 == 0):
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')