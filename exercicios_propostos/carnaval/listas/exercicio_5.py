"""
How Bootcamps - Stone - /código[s]
Data: 01/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 5:

Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
adicione o elemento 7000 logo após o elemento 6000 na lista acima. 
O resultado final deverá ser:
>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""
# Definindo a lista
lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 

# inserindo o valor desejado na lista
lst[2][2].append(7000)

# Imprimindo a nova lista
print(lst)