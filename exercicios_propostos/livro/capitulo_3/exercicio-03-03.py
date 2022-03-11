"""
How Bootcamps - Stone - /código[s]
Data: 06/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python
Exercício 03-03: Complete a tabela a seguir utilizando a = True, b = False e c = True
Complete a tabela a seguir utilizando a = True, b = False e c = True.

Expressão Resultado         Expressão Resultado
a and a   ○ True ○ False    a or c    ○ True ○ False
b and b   ○ True ○ False    b or c    ○ True ○ False
not c     ○ True ○ False    c or a    ○ True ○ False
not b     ○ True ○ False    c or b    ○ True ○ False
not a     ○ True ○ False    c or c    ○ True ○ False
a and b   ○ True ○ False    b or b    ○ True ○ False
b and c   ○ True ○ False
"""
# Definindo as variaveis
a = True 
b = False
c = True

# Imprimindo a tabela
print('For a = True, b = False e c = True\n')
print('\nExpressão     |  Resultado')
print(f'\na and a       |  {a and a}')
print(f'\nb and b       |  {b and b}')
print(f'\nnot c         |  {not c}')
print(f'\nnot b         |  {not b}')
print(f'\nnot a         |  {not a}')
print(f'\na and b       |  {a and b}')
print(f'\nb and c       |  {b and c}')
print(f'\na or c        |  {a or c}')
print(f'\nb or c        |  {b or c}')
print(f'\nc or a        |  {c or a}')
print(f'\nc or b        |  {c or b}')
print(f'\nc or c        |  {c or c}')
print(f'\nb or b        |  {b or b}')