"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição

Exercício 1

Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário 
e imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.

Atenção!
Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!
"""

print('Digite os valores dos quais voce deseja calcular a média, e quando acabar digite 0, você deve digita ao menos um valor valido!')
valores = []

valor = int(input('Digite um valor: '))

while valor == 0:
    print('Você deve digitar pelo menos um valor valido!')
    valor = int(input('Digite um valor: '))
    
while valor != 0:
    valores.append(valor)
    valor = int(input('Digite um valor: '))

media = sum(valores) / len(valores)

print(f'A média dos valores fornacidos é: {media}')