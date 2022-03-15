"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: laço de repetição


Exercício 3:

Um determinado zoológico cobra a entrada com base na idade do visitante. 
Os visitantes com 2 anos de idade ou menos não pagam para entrar. 
Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. 
A entrada para todos os outros visitantes é de R$23,00. 
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, 
com uma idade inserida em cada linha. 
O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo. 
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada. 
O custo deve ser exibido usando duas casas decimais.
"""
print('\nPara calcular o valor das entradas, digite a idade das pessoas no grupo! No final entre um valor em branco!')

idades = []
crianca = 14.00
idoso = 18.00
adulto = 23.00
valor_total = 0

idade = input('Digite a idade do visitante: ')
while idade == '':
    print('Voce deve digitar a idade de pelo menos um visitante!')
    idade = input('Digite a idade do visitante: ')
    
while idade != '':
    idades.append(int(idade))
    idade = input('Digite a idade do visitante: ')
    
for idade in idades:
    if idade < 3:
        valor_total += 0
    elif idade <= 12:
        valor_total += crianca
    elif idade < 65:
        valor_total += adulto
    else:
        valor_total += idoso

print(f'O valor total das entradas é R${valor_total:.2f}')