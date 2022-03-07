"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Desafios
Diversão do carnaval \o/

Desafio 2:
    
Implemente um jogo em que o usuário tenha que adivinhar o somatório de dois dados.
1.	O jogo deve sortear um número para cada dado. Estes números devem variar entre 1 e 6, inclusive. 
    Deve-se calcular a soma dos dois valores.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: 
    não pode ser inferior a 2 ou superior a 12. 
    Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado e o resultado da jogada deve ser apresentado na tela:
a.	Caso o usuário informe um número superior ou inferior à soma dos dados, 
    o jogo deve apresentar a mensagem “Você errou. A soma dos dados é x. 
    O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo x o valor da soma, 
    d1 o valor do primeiro dado e d2 o valor do segundo dado.
b.	Caso o usuário informe um número igual ao valor da soma, 
    o jogo deve apresentar a mensagem “Parabéns! Você acertou a soma dos dados! 
    O valor do primeiro dado é d1 e o do segundo é d2. ”, 
    sendo d1 o valor do primeiro dado e d2 o valor do segundo dado
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. 
    Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

Dica!
Pesquise sobre o módulo buit-in do Python chamado random
"""
# Importando o modulo random
import random

# Definindo a função jogo
def jogo():
    
    # Gerando os números aléatorios entre 1 e 6 e somando eles
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma = dado_1 + dado_2
    
    # recebendo o numero do usúario
    numero = int(input('Digite o valor da sua aposta! O valor deve estar entre 2 e 12: '))
    
    # validando o numero digitado
    while numero > 12 or numero < 2:
        
        # pedindo para o usúario digitar outro numero, caso o primeiro esta fora do range
        numero = int(input('Você digitou um numero fora do range aceito. Digite um numero entre 2 e 12: '))
        
    # checando se o numero do usúario corresponde ao numero sorteado
    if numero == soma:
        print(f'\nParabéns! Você acertou a soma dos dados! O valor do primeiro dado é {dado_1} e o do segundo é {dado_2}.')
    else:
        print(f'\nVocê errou. A soma dos dados é {soma}. O valor do primeiro dado é {dado_1} e o do segundo é {dado_2}. ')
        
    jogar()
    
# Definindo a função jogar
def jogar():
    # pergunta pro usuario se ele quer ou não continuar jogando
    resposta = input('Você deseja continuar jogando? sim[s], não[n] ').lower()
    respostas = ['s', 'n']
    
    # Validando a resposta
    while resposta not in respostas:
        resposta = input("Você deseja continuar jogando? Sua resposta deve ser 's' para sim ou 'n' para não: ").lower()
   
    # se a resposta for sim, chama a função jogo
    if resposta == 's':
        jogo()
    # se a resposta for não, imprime a mensagem e encerra o programa    
    elif resposta == 'n':
        print('Jogo encerrado')
        
if __name__=='__main__':
    jogo()
