"""
How Bootcamps - Stone - /código[s]
Data: 08/03/2022
Autor: Camila Rodrigues Costa
Descrição: Estrutura de repetição (for e while)
"""
alunos = dict()
# continuar = ('s', 'n')

nome = input("Digite o nome do aluno: ")

alunos[nome] = []

condicao = 'S'

while condicao == 'S':
    nota = float(input('Digite uma nota: '))
    alunos[nome]
    condicao = input('Deseja entrar com outra nota? S ou N?').upper()