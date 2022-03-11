"""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Autor: Camila Rodrigues Costa
Descrição: Funções
"""
# Usando um exemplo mais simples 
def soma(a, b: int = 10):
    return a + b

c = soma(5)
d = soma(b=8, a=4)

print(c, d)