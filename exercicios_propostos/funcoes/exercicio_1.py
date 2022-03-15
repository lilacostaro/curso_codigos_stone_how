"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: Funções

Exercício 1:

Em um determinad país, as tarifas de táxi consistem em uma tarifa básica 
de R$4,00 mais R$0,25 para cada 140 metros percorridos. 
Escreva uma função que receba a distância percorrida (em quilômetros) como único 
parâmetro e retorna a tarifa total como único resultado. 
Escreva um programa que demonstre o uso da sua função.
"""
km = float(input('Digite a quantidade de kms percorridos: '))

def valor(distancia):
    tarifa = 4.00
    tarifa_extra = 0.25
    metros = distancia * 1000
    extra = (metros // 140) * tarifa_extra
    total = tarifa + extra
    
    return total

if __name__=='__main__':
    print(valor(km))
    print(valor(9.8))
    print(valor(12.45))
    