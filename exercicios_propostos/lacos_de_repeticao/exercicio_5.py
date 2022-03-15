"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição

Exercício 5:

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta 
em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informadas ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""
atleta = input('Digite o nome do atleta: ')

notas = []

for i in range(1,8):
    nota = float(input(f'Digite a nota do {i}° jurado: '))
    notas.append(nota)
    
nota_max = max(notas)
nota_min = min(notas)


notas.pop(notas.index(nota_max))
notas.pop(notas.index(nota_min))

media = sum(notas) / len(notas)

print('\nResultado final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {nota_max}')
print(f'Pior nota: {nota_min}')
print(f'Média: {media:.2f}')
