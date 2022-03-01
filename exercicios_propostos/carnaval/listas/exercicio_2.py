"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 2:

Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
>>> [[7,7,7], “H”, 6, 3, 1]
"""
# Definindo a lista
lista = ['Camila', 
         27, 
         {'nome': 'Camila', 'idade': 27}, 
         (3, 5, 7), 
         [8, 2, 1], 
         {'livro': 'Jogos Vorazes', 'autor': 'Suzanne Collins'},
         'Harry Potter',
         2022,
         '#f%w25',
         '01-03-2022']


# iterando a lista e imprimindo o resultado
for i in range(1,11):
    print(f'Elemento {lista[-i]} na posição {-i}')