"""
How Bootcamps - Stone - /código[s]
Data: 05/04/2022
Autor: Camila Rodrigues Costa
Enunciado: Desenvolver um programa para sortear brindes para um determinado grupo de pessoas.
"""
import csv
from collections import defaultdict
from random import choice

brinds = {"how": 5, "stone": 13}
equipes = defaultdict(list)
pessoas_nao_sorteadas = []

with open(r'aulas\aula_05-04-2022\Sorteio.csv') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=',', quotechar='|')
    for linha in arquivo:
        if linha[0] == "Nome do Aluno":
            continue 
        nome_aluno = linha[0].strip().replace('  ', ' ')
        numero_equipe = int(linha[1])
        equipes[numero_equipe].append(nome_aluno)  
        
# print(equipes.keys())    

# 1 - 40 -> 2 sorteios stone 
# 1 - 40 -> 1 sorteio how
# 3 pessoas -> 3 brinds individuais da stone 

for _ in range(2):
    print('Sorteio do brind da stone!')
    equipe_sorteada = choice(list(equipes.keys()))
    print(f'\nA equipe sorteada foi {equipe_sorteada}...')
    for pessoa in equipes[equipe_sorteada]: 
        print(f'Parabéns {pessoa} ganhou um brind da stone!')
        # pessoas_sorteadas.append(pessoa)

    equipes.pop(equipe_sorteada)
    print('*' * 60)
    
print('Sorteio do brind da how!')
equipe_sorteada = choice(list(equipes.keys()))
print(f'\nA equipe sorteada foi {equipe_sorteada}...')
for pessoa in equipes[equipe_sorteada]: 
    print(f'Parabéns {pessoa} ganhou um brind da how!')
    # pessoas_sorteadas.append(pessoa)

equipes.pop(equipe_sorteada)
print('*' * 60)
  
# print(equipes.keys())

for lista_nomes in equipes.values():
    pessoas_nao_sorteadas.extend(lista_nomes)
    
# print(f'\nPessoas não sorteadas: {pessoas_nao_sorteadas}')

for _ in range(3):
    
    pessoa_sortuda = choice(pessoas_nao_sorteadas)
    
    pessoa_sortuda_indice = pessoas_nao_sorteadas.index(pessoa_sortuda)
    
    print(f'\nParabéns {pessoa_sortuda} voce ganhou um brind individual da stone!')
    
    pessoas_nao_sorteadas.pop(pessoa_sortuda_indice)