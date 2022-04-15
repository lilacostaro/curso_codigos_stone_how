"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 2
"""

from poo_2 import Funcionario

funcionario1 = Funcionario("Camila", "Costa", 7000.00)

funcionario1.salario_inicial = 10000.00

print(funcionario1.salario_inicial)

funcionario1.dar_aumento()