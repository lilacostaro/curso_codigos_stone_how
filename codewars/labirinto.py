"""
Desafio Labirinto Codigo[s]
"""

from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "."
CAMINHO_VOLTA = ","
ROBO = "X"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    nova_posicao = posicao[0] + direcao[0], posicao[1] + direcao[1]
    return nova_posicao
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    nova_posicao = posicao[0] + direcao[0], posicao[1] + direcao[1]
    if LABIRINTO[nova_posicao[0]][nova_posicao[1]] == PAREDE:
      return False
    return True

def main():
    usuario = input("Digite uma linha e uma coluna para a posição inicial do robô separados por vírgula: ").split(",")
    lin, col = int(usuario[0]),  int(usuario[1])
    posicao = [lin, col]
    while (LABIRINTO[posicao[0]][posicao[1]]) == PAREDE or (LABIRINTO[posicao[0]][posicao[1]] == SAIDA):
        usuario = input("Digite uma linha e uma coluna para a posição inicial do robô separados por vírgula: ").split(",")
        lin, col = int(usuario[0]),  int(usuario[1])
        posicao = [lin, col]
    POSICAO_INICIAL = posicao

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL
    # direcoes = [DIREITA, ESQUERDA, CIMA, BAIXO]
    # for i in direcoes:
    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
        print_labirinto()
        sleep(1)

if __name__ == "__main__":
    main()
    #movimento((1, 1), CIMA)