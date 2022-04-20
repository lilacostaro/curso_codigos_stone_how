"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 3
"""
class Employee:
    
    roles = ('jr', 'pl','sr')
    
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        
    def __eq__(self, other: object) -> bool:
        return (self.salary == other.salary) and (self.name == other.name)
    
    # >= maior-ou-igual -> greater-than-or-equal -> ge    
    def __ge__(self, other: object) -> bool:
        return self.salary >= other.salary
    
    # <= menor-ou-igual -> less-than-or-equal -> le    
    def __le__(self, other: object) -> bool:
        return self.salary <= other.salary
    
    # < menor -> less -> lt    
    def __lt__(self, other: object) -> bool:
        return self.salary < other.salary
    
    # > maior -> greater -> gt   
    def __gt__(self, other: object) -> bool:
        return self.salary > other.salary
    
    def __add__(self, other: object) -> object:
        return self.salary + other.salary
    
    def __sub__(self, other: object) -> object:
        return self.salary - other.salary

        
emp1 = Employee('Camila', 5500)
emp2 = Employee('Camila', 6000)



# __eq__
print(emp1 == emp2)
print(emp1 != emp2)

# __ge__
print(emp1 >= emp2)
# __le__
print(emp1 <= emp2)
# __lt__
print(emp1 < emp2)
# __gt__
print(emp1 > emp2)

print(id(emp1))
print(id(emp2))

print('Exemplo mundo real')

class Ciclo:
    ciclos = [202117, 202201, 202202, 202203, 202204, 2023]
    
    def __init__(self, ciclo) -> None:
        self.ciclo = ciclo
        
    def __add__(self, n):
        return Ciclo.ciclos[Ciclo.ciclos.index(self.ciclo) + n]
    
c = Ciclo(202117)

print(c + 1)