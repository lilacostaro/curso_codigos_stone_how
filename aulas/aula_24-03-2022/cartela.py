from collections import defaultdict
from random import randint
from prettytable import PrettyTable

LETRAS = ('B', 'I', 'N', 'G', 'O')


def min_max(letra):
    # Coletar o numero minimo e maximo de cada letra
    intervalo = {'B': (1, 15), 'I': (16, 30), 'N': (31, 45), 'G': (46, 60), 'O': (61, 75)}
    maximo, minimo = intervalo[letra][1], intervalo[letra][0]
    return minimo, maximo
    
# Passo numero 0:
def gera() -> defaultdict[str, list[int]]:
    """Gera uma cartela com 5 números aleatórios para cada letra"""

    cartela = defaultdict(list)

    for letra in LETRAS:
        
        minimo, maximo = min_max(letra)
        
        while len(cartela[letra]) < 5:
            # Gerar um número aleatório
            num_aleatorio = randint(a=minimo, b=maximo)
            
            # Verificar se o numero não existe naquela letra
            if num_aleatorio in cartela[letra]:
                continue
            
            # Colocar número aleatorio na lista 
            cartela[letra].append(num_aleatorio)
            
            # Ordenar em  ordem crescente os números
            cartela[letra].sort()
    
    return cartela

# Passo numero 1:
def imprime(cartela: dict[str,  list[int]]) -> None:
    """Formata a cartela para imprimir na tela"""
    cabecalho = [letra for letra in 'BINGO']
    row = []
    for linha in range(5):
        row.append([str(lista[linha]).zfill(2) for lista in cartela.values()])
        
    # print(row)
    x = PrettyTable()
    x.field_names = cabecalho
    for y in range(len(row)):
        x.add_row(row[y])

    print(x)