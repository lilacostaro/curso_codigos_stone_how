"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Camila Costa
Enunciado: POO - Introdução
"""
from pessoas import Funcionario

funcionario1 = Funcionario('Camila', 'Rodrigues Costa', 2000)

funcionario2 = Funcionario('João', 'Silva Castro', 3000)

funcionario3 = Funcionario('Maria', 'Santos', 4000)

funcionario4 = Funcionario('Pedro', 'Santos')

print(type(funcionario1))
print(funcionario1.nome)
print(funcionario1.sobrenome)
print(funcionario1.salario_inicial)


funcionario1.dar_aumento()
funcionario2.dar_aumento()
funcionario3.dar_aumento()

print(funcionario1.salario_atual)
print(funcionario2.salario_atual)
print(funcionario3.salario_atual)


funcionario1.dar_aumento()
print(funcionario1.salario_atual)

funcionario1.dar_aumento()
print(funcionario1.salario_atual)

print('\n\nSalario funcionrio 4')
print(funcionario4.salario_inicial)
funcionario4.dar_aumento()
print(funcionario4.salario_atual)
funcionario4.dar_aumento()
print(funcionario4.salario_atual)
funcionario4.dar_aumento()
print(funcionario4.salario_atual)