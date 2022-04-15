"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Camila Costa
Enunciado: POO - Aula 2
"""
class Funcionario:
    
    aumento_percentual: float = 0.1
    
    # Dois underlines!
    # Método construtor
    def __init__(self, nome: str, sobrenome: str,  salario_inicial: float = 1200.00):
        self.nome : str = nome
        self.sobrenome : str = sobrenome
        self.__salario_inicial : float = salario_inicial
        
        self.email : str = f"{self.nome.lower()}.{self.sobrenome.lower().split()[-1]}@empresa.com"
        
    # def dar_aumento(self, porcentagem: float) -> None:
    #     if hasattr(self, 'salario_atual'):
    #         self.salario_atual = self.salario_atual * (1 + porcentagem)
    #     else:
    #         self.salario_atual = self.salario_inicial * (1 + porcentagem)
    
    @property
    def salario_inicial(self) -> float:
        return self.__salario_inicial
    
    def dar_aumento(self) -> None:
        """Amplia o salário do funcionário em 10%. 
        O novo salário será definido no atributo salario_atual"""
        if hasattr(self, 'salario_atual'):
            self.salario_atual = self.salario_atual * (1 + Funcionario.aumento_percentual)
        else:
            self.salario_atual = self.__salario_inicial * (1 + Funcionario.aumento_percentual)
            
            
