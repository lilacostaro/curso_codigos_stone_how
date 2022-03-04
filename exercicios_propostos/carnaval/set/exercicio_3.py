"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e Sets
Diversão do carnaval \o/

Exercício 3:

Faça um programa que ordene um dicionário por seus valores. 
Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

"""
notas = {'matemática': 81, 'física': 83, 'química': 87, 'história': 85, 'geografia': 89} 
notas_ordenadas = dict(sorted(notas.items(), key=lambda nota: nota[1], reverse=True))

print(notas_ordenadas)