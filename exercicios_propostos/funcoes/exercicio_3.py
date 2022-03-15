"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: Funções

Exercício 3:

Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""
valor = input("Digite um munero inteiro com pelo menos 3 digitus: ")

def num_reverso(num):
    reverse_num = num[::-1]
    return reverse_num
    

if __name__=='__main__':
    print(num_reverso(valor))