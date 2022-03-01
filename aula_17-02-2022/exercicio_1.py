"""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Camila Rodrigues Costa
Descrição: Introdução a sintaxe e tipos de dados
"""
nome = 'Camila Rodrigues Costa' #input('Digite o nome do(a) aluno(a): ')

nota1 = float(input('Digite a 1ª nota: '))

nota2 = float(input('Digite a 2ª nota: '))

nota3 = float(input('Digite a 3ª nota: '))

media = (nota1 + nota2 + nota3) / 3

media_round = round(media)


print(f'\nO(a) aluno(a) {nome} alcancou a média {media_round}!')
# print(type(media))
