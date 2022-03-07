"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Desafios
Diversão do carnaval \o/

Desafio 1:

Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

1.	O jogo deve sortear um número entre 1 e 100.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: 
    não pode ser inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, 
    o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado:
a.	Caso o usuário informe um número inferior ao número sorteado, 
    o jogo deve apresentar a mensagem “O número sorteado é maior.”.
b.	Caso o usuário informe um número superior ao número sorteado, 
    o jogo deve apresentar a mensagem “O número sorteado é menor.”.
c.	Caso o usuário informe um número igual ao número sorteado, 
    o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” 
    e o jogo deve ser finalizado, sendo apresentado ao usuário a quantidade de tentativas efetuadas 
    até este momento.
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. 
    Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

Dica!
Pesquise sobre o módulo buit-in do Python chamado random
"""
# Importando o modulo random
import random

# Definindo a função jogo
def jogo():
    print('Novo Jogo!')
    # Gerando um numero aleatorio entre 0 e 100
    random_number = random.randint(0, 100)
    
    # Definindo a variavel tentativas, com o valor inicial de 1
    tentativas = 1
    
    # recebendo o numero do usúario
    numero = int(input('Digite um numero entre 0 e 100: '))
    
    # validando o numero digitado
    while numero > 100 or numero < 0:
        # pedindo para o usúario digitar outro numero, caso o primeiro esta fora do range
        numero = int(input('Você digitou um numero fora do range aceito. Digite um numero entre 0 e 100: '))
    # checando se o numero do usúario corresponde ao numero sorteado
    while numero != random_number:
        
        # se o numero do usuario for menor, o programa fara isso
        if numero < random_number:
            # aumenta 1 nas tentativas
            tentativas = tentativas + 1
            # imprimir a mensagem de numero muito baixo
            print('Desculpe, tente novamente. Numero muito baixo.')
            # pedir pro usuario digitar um novo numero
            numero = int(input('Digite um numero entre 0 e 100: '))
        
        # se o numero for maior o programa fara o mesmo que fez no caso anterior
        elif numero > random_number:
            tentativas = tentativas + 1
            print('Desculpe, tente novamente. Numero muito alto.')
            numero = int(input('Digite um numero entre 0 e 100: '))
    
    # Se o numero for igual ele printa o valor correto e a quantidade de tentativas            
    print(f'Parabéns. voce acertou o numero {random_number} em {tentativas} tentativas.')
    
    # chama a função jogar
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

    
    
    
    
    
    
    
    