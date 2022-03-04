"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e Sets
Diversão do carnaval \o/

Exercício 5:

Faça um programa que encontre as notas mínimas e máximas de um dicionário, 
e imprima-os na tela com as suas respectivas chaves. 
Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20
"""
# definindo o dicionario
dic = {'Theodoro': 20, 'Márcia': 50, 'Júnior': 80, 'Camila': 100, 'Ana': 90, 'Vinicius': 30}

# Encontrando os valores maximo e minimo
minimo = min(dic.items(), key=lambda nota: nota[1])
maximo = max(dic.items(), key=lambda nota: nota[1])

# Imprimindo o resultado
print(f'\nNota máxima -> {maximo[0]} : {maximo[1]}')
print(f'Nota mínima -> {minimo[0]} : {minimo[1]}')

# Encontrando os valores maximo e minimo
valores = list(dic.values())
maximo_1 = max(valores)
minimo_1 = min(valores)

# Imprimindo o resultado
for k, v in dic.items():
    
    if v == minimo_1:
        print(f'\nNota mínima -> {k} : {v}')
    
    if v == maximo_1:
        print(f'\nNota máxima -> {k} : {v}')
    