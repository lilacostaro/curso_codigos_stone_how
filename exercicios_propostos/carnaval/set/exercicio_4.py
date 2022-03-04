"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e Sets
Diversão do carnaval \o/

Exercício 4:

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. 
Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6} 
"""
# Definindo o dicionario
dic = {1: 'vermelho', 2: 'azul', 3: 'marrom', 4: 'roxo', 5: 'lilas', 6: 'alaranjado'}
# Definindo um dicionario vazio
dic_2 = {}

# Varendo todo dic
for k,v in dic.items():
    # Adicionando os valores ao dic_2
    dic_2[k] = len(v)
 
# Imprimindo o resultado    
print(dic_2)