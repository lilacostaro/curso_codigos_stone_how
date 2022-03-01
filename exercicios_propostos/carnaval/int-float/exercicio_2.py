"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: tipos numéricos
Diversão do carnaval \o/

Exercício 2:

Faça um programa que receba a base e altura de um triângulo e imprima a área dele.
Dica!
A área de um triângulo é dada pela seguinte fórmula: area = (base x altura) / 2
"""
# Recebendo as informaçoes do usuario
base = int(input('Digite o valor da base cm: '))
altura = int(input('Digite o valor da aultura cm: '))

# Função da area do triangulo
area = (base * altura) / 2

# Imprimindo a resposta
print(f'A área do tiango de base {base} e altura {altura} é {area}cm2')