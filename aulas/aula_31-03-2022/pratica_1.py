"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Camila Rodrigues Costa
Enunciado: Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from random import choice

from list_words import WORDS_LIST, STATUS, generate_word


def get_secret_word(words: list) -> str:
    """Devolve uma palavra aleatória de uma lista."""
    return choice(words).upper()


def print_game_board(secret_word: str, 
                     correct_letters: list, 
                     wrong_letters: list, 
                     error: int, 
                     attempts: int, 
                     status: list):
    """Imprime a situação atual do jogo."""
    encoded_word = ''

    for letter in secret_word:
        if letter not in correct_letters:
            encoded_word += '-'
        else:
            encoded_word += letter
            
    if error <= 6:
        print(status[error])
        
        print(encoded_word)
    
    print(f'\nLetras corretas: {" ".join(correct_letters)}')
    print(f'\nLetras erradas: {" ".join(wrong_letters)}')

def read_input_player():
    """Lê uma letra do usuário."""
    letter = input('\nDigite uma letra: ')
    
    while len(letter) != 1:
        print('Digite apenas uma letra!')
        letter = input('\nDigite uma letra: ')
    return letter.upper()


def guess_letter(secret_word, letter, correct_letters, wrong_letters):
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
    if letter in secret_word:
        print(f'A letra {letter} está na palavra!')
        correct_letters.append(letter)
        secret_word.remove(letter)
        return True
    elif (letter in correct_letters) or (letter in wrong_letters):
        print('\nVocê já jogou a letra {letter}!')
        return False
    else:
        print(f'A letra {letter} não está na palavra!')
        wrong_letters.append(letter)
        return False


def game_continue(secret_word, attempts, correct_word):
    """Função que decide se jogo já encerrou ou não."""
    if secret_word and attempts > 0:
        return True
    elif not secret_word and attempts > 0:
        print(f'\nParabéns! Você ganhou! A palavra era "{correct_word}"')
        return False
    else:
        print(STATUS[-1])
        print(f'\nA palavra era: {correct_word}\n')
        return False


# secret_word = get_secret_word(WORDS_LIST)
secret_word = generate_word()
secret_word2 = set(secret_word) # variável para palavra secreta
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue(secret_word2, attempts, secret_word):
    print_game_board(secret_word, correct_letters, missed_letters, error, attempts, STATUS)
    letter  = read_input_player()
    if not guess_letter(secret_word2, letter, correct_letters, missed_letters):
        error += 1
        attempts -= 1
    print("\nTentativas restantes: ", attempts)
