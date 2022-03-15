"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Lista de exercícios
Tema: Funções

Exercício 4:

Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra 
string com os carateres embaralhados. Por exemplo: se função receber a palavra python, 
pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, 
independentemente de como foram digitados.
"""
import random

word = input('Digite uma palavra: ').lower()

def embaralhar(word): 
    return "".join(random.sample(word, len(word)))


if __name__=='__main__':
    print(embaralhar(word))
