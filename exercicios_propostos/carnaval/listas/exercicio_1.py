"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 1:

Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3
"""
# Definindo a lista
lista = ['Camila', '27', {'nome': 'Camila', 'idade': 27}, (3, 5, 7), [8, 2, 1]]

# iterando a lista e imprimindo o resultado
for i,j in enumerate(lista):
    print(f'Elemento {j} na posição {i}')
