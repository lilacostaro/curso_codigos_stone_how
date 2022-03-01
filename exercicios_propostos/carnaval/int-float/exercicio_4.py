"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: tipos numéricos
Diversão do carnaval \o/

Exercício 4:

Faça um programa que receba do usuário seu peso em kg e altura em metros 
e imprima o Índice de Massa Corporal (IMC) do usuário.
Dica!
O IMC é calculado de acordo com a fórmula: IMC = peso / (altura ** 2)
"""
# Recebendo os dados do usuario
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))

# Calculando o IMC
imc = peso / (altura ** 2)

# Imprimindo o resultado
print(f'O seu IMC é {imc:.2f}')