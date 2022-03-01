"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 3:

Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. 
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""
# Definindo a lista
lista = [1, -7, 2, 4, 11, -3]

# Encontrando os valores maximo e minimo
minimo = min(lista)
maximo = max(lista)

# Encontrando os indices
ind_min = lista.index(minimo)
ind_max = lista.index(maximo)

# imprimindo os resultados
print(f'\nO maior elemento é {maximo} e está na posição {ind_max}')
print(f'O menor elemento é {minimo} e está na posição {ind_min}')
