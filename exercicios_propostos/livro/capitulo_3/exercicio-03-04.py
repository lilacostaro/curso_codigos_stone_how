"""
How Bootcamps - Stone - /código[s]
Data: 06/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python
Exercício 03-04: Crie uma expressão para determinar se uma pessoa deve ou não pagar imposto

Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
"""
def Salario(salario):
    if salario > 1200.00:
        print(f'Seu salário é {salario} então você deve pagar imposto!')
    else:
        print(f'Seu salário é {salario} então você não precisa pagar imposto!')

if __name__=='__main__':
    Salario(1500)
    Salario(750)
    Salario(850)
    Salario(3200)
    Salario(1200)
    Salario(250)
    Salario(400)