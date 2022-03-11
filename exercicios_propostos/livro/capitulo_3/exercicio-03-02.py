"""
How Bootcamps - Stone - /código[s]
Data: 06/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python
Exercício 03-02: Complete a tabela com o resultado da expressão booleana correspondente
Complete a tabela a seguir, respondendo True ou False. 
Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

Expressão Resultado        Expressão Resultado
a == c    ○ True ○ False   b > a     ○ True ○ False
a < b     ○ True ○ False   c >= f    ○ True ○ False
d > b     ○ True ○ False   f >= c    ○ True ○ False
c != f    ○ True ○ False   c <= c    ○ True ○ False
a == b    ○ True ○ False   c <= f    ○ True ○ False
c < d     ○ True ○ False
"""
# Declarando as variaveis
a = 4
b = 10 
c = 5.0
d = 1
f = 5

# Imprimindo os resultados
print('For a = 4, b = 10, c = 5.0, d = 1 e f = 5\n')
print('\nExpressão     |  Resultado')
print(f'\na == c        |  {a == c}')
print(f'\na < b         |  {a < b}')
print(f'\nd > b         |  {d > b}')
print(f'\nc != f        |  {c != f}')
print(f'\na == b        |  {a == b}')
print(f'\nc < d         |  {c < d}')
print(f'\nb > a         |  {b > a}')
print(f'\nc >= f        |  {c >= f}')
print(f'\nf >= c        |  {f >= c}')
print(f'\nc <= c        |  {c <= c }')
print(f'\nc <= f        |  {c <= f }')