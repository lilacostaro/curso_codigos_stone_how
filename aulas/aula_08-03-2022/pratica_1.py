"""
How Bootcamps - Stone - /código[s]
Data: 08/03/2022
Autor: Camila Rodrigues Costa
Descrição: Estrutura de repetição (for e while)
"""
# Declarando o dicionario alunos
alunos = {}

# Declarando a variavel nota_minima
nota_min = 7

# Perguntando ao usuario quantos alunos serão adicionados
numero_alunos = int(input("Quantos alunos você irá digitar? "))
# Perguntando para o usuario quantas notas serão digitadas por aluno
numero_notas = int(input('Digite a quantidade de notas por aluno: '))

# Loop externo que ira pegar o nome do aluno
for i in range(1, numero_alunos+1):
    # declarando um lista vazia que receberá as notas
    notas = []
    # Recebendo o nome do aluno
    nome = input(f'Digite o nome do {i}° aluno: ')
    # Loop inteno que receberá as notas
    for nota in range(1, numero_notas+1):
        # Recebendo as noas
        nota = float(input(f'Digite a {nota}ª nota do aluno: '))
        # Validando as notas, elas precisam estar entre 0 e 10
        while nota < 0 or nota > 10:
            # caso a nota não seja validada, outra nota sera requisitada
            nota = float(input('Nota fora do range, digite uma nota entre 0 e 1: '))
        # uma vez que a nota for validada, ela será adicionada a lista notas
        notas.append(nota)
    # Uma vez que tudo for validado, o nome sera adicionado ao dicionario como chave e as notas como valor
    alunos[nome] = notas

# loop para imprimir a média de cada aluno
for aluno, notas in alunos.items():
    # Calculando a média de cada aluno
    media = sum(notas) / len(notas)
    if media > nota_min:
        print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi aprovado!')
    else:
        print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi reprovado!')