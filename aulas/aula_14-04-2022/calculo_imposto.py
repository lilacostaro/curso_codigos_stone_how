"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 2
"""

from imposto import ICMS, ISS, IPI, COFINS, Imposto

class Venda:
    
    def __init__(self, valor_bruto : float, imposto : Imposto) -> None:
        self.valor_bruto = valor_bruto
        self.imposto: Imposto = imposto
        
        
    def calcular_valor_liquido(self) -> float:
        return self.imposto.calcula(self.valor_bruto)
    
venda = Venda(1000, IPI())

venda2 = Venda(1000, ICMS())

v3 = Venda(105800, ISS())
v4 = Venda(1058800, COFINS())

print(venda.calcular_valor_liquido())
print(venda2.calcular_valor_liquido())
print(v3.calcular_valor_liquido())
print(v4.calcular_valor_liquido())

print(venda.imposto)