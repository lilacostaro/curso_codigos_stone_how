"""
How Bootcamps - Stone - /código[s]
Data: 22/02/2022
Autor: Camila Rodrigues Costa
Descrição: Introdução a listas, tuplas e sets.
Dica da tia Fer: para armazenar valores, podem ser usadas variáveis, listas e tuplas. Uma variável guarda um único valor; listas e tuplas podem guardar vários valores. As listas podem ser manipuladas (pode-se inserir elementos, remover elementos, ordenar a lista, ...). As tuplas apenas guardam os valores, sem a possibilidade de ter seus elementos alterados.
"""
nome = 'Camila Rodrigues Costa'

nota = input('Digite as notas do aluno: ').split(',')
notas = []
for i in nota:
    i = float(i)
    notas.append(i)
    
    
print(notas)

media = sum(notas) / len(notas)
# print(nome.split())
# print(notas)
print(f'A média do aluno foi: {media:.2f}')