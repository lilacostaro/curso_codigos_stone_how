"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 3
"""
d = {'nome': 'Camila'}
a = 1
b = 10

try:
    print(a/b)
    print(d['sobrenome'])
except KeyError:
    print(KeyError('Chave não encontrada'))
except ZeroDivisionError:
    print('Capturei meu ZeroDivisionError')
except Exception as e:
    print(e)
    
print('Fim')

# Má pratica except: pass

class SalaryNotInRangeError(Exception):
    """Exceção gerada quando o salário não está dantro da faixa específicada
    
    Attributes:
        salary (int): salário que gerou o erro
        message (str): mensagem ao usuário
    """
    
    def __init__(self, salary, message='Salário não está na faixa específicada (5000, 15000)'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'Salário: {self.salary} -> {self.message}'
    
salary = int(input('Digite o seu salário: '))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
print(f'Salário {salary} ok')