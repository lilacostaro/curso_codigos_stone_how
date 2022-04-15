"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 2
"""

class Imposto:
    def calcula(self):
        pass

class ICMS:
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.05)
    
    def __str__(self):
        """Print da classe ICMS"""
        return 'Imposto ICMS'
        
    def __repr__(self):
        """Represenatação da classe ICMS"""
        return 'Imposto ICMS'
    
    
class ISS:
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.10)
    
class IPI:
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.15)
    
class COFINS:
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.20)