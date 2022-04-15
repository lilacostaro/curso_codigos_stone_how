class Ave:
    
    def __init__(self, numero_de_patas, cor, tamanho) -> None:
        self.numero_de_patas = numero_de_patas
        self.cor = cor
        self.tamanho = tamanho
        
    def voar(self) -> None:
        print('Ave voando!')
        
class Tuacano(Ave):
    def __init__(self, mancha_no_olho):
        super().__init__(2, 'Colorido', 'Médio Porte')
        
        self.tem_mancha_no_olho = mancha_no_olho
        
    def voar(self) -> None:
        print('Voando como um Tucano!')


corvo = Ave(2, 'Preto', 'Pequeno')

t = Tuacano(True)

corvo.voar()
t.voar()

print(t.tem_mancha_no_olho)