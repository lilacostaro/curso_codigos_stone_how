"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: tipos numéricos
Diversão do carnaval \o/

Exercício 5:

Escrevaum programa que leia do usúario um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3 + 1 + 4 + 1 = 9
"""
# Recebendo o input do usuario
num = input("Digite um número de 4 dígitos: ")

# Declarando uma lista vazia que recebera os numeros digitados
numeros = []

# separando e convertendo os numeros recebidos de str para int
separando = [numeros.append(int(num[i])) for i in range(len(num))]

# somando os valores
soma = sum(numeros)

# imprimindo o resultado
print(f'\n{numeros[0]} + {numeros[1]} + {numeros[2]} + {numeros[3]} = {soma}')