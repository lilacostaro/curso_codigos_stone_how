from urllib.request import Request, urlopen
from bs4 import *
import string

WORDS_LIST = ['python', 
             'java', 
             'kotlin', 
             'javascript', 
             'bootcamp', 
             'programacao']

def generate_word():
    idioma_palavras = input('''
Escolha uma das opções de idioma abaixo:

1  - Árabe
2  - Alemão
3  - Catalão
4  - Dinamarquês
5  - Espanhol
6  - Finlandês
7  - Francês
8  - Holandês
9  - Inglês
10 - Italiano
11 - Português
12 - Sueco

Digite o número da opção escolhida: ''')

    if idioma_palavras == '1':
        idioma = 'kalimat-eashwayiya'
    elif idioma_palavras == '2':
        idioma = 'zufallige-worter'
    elif idioma_palavras == '3':
        idioma = 'paraula-aleatoria'
    elif idioma_palavras == '4':
        idioma = 'tilfaeldige-ord'
    elif idioma_palavras == '5':
        idioma = 'index'
    elif idioma_palavras == '6':
        idioma = 'satunnaiset-sanat'
    elif idioma_palavras == '7':
        idioma = 'mots-aleatoires'
    elif idioma_palavras == '8':
        idioma = 'willekeurige-woorden'
    elif idioma_palavras == '9':
        idioma = 'random-words'
    elif idioma_palavras == '10':
        idioma = 'parole-casuali'
    elif idioma_palavras == '11':
        idioma = 'palavras-aleatorias'
    elif idioma_palavras == '12':
        idioma = 'slumpade-ord'
    
    categorias = int(input('''
Escolha uma das categorias abaixo:

0  - Dicionário completo
1  - Dicionário para crianças
2  - Alimentos
3  - Animais
4  - Cores
5  - Corpo humano
6  - Educação
7  - Família
8  - Figuras geométricas
9  - Mídia de comunicação        
10 - Profissões
11 - Transporte

Digite o número da opção escolhida: '''))

    if categorias == 10:
        categoria = 12
    elif categorias == 11:
        categoria = 13
    else:
        categoria = categorias
    n_palavras = 1
    url = f'https://www.palabrasaleatorias.com//{idioma}.php?fs={n_palavras}&fs2={categoria}&Submit=Nova+palavra'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    teste = urlopen(req).read()
    data = teste.decode('utf-8') #Precisa de decodificação para que os acentos apareçam
    soup = BeautifulSoup(data, "html.parser")

    data1 = soup.find_all('div') #Encontra todas as tags <div> </div> e mostra em formato de lista
    word = data1[1] # pega somente o elemntos da lista que contém a palavra gerada
    
    word = word.string # acessa o conteudo da tag
    
    """a plavra estava retornando no formato '\n\r*******' 
    este passo é para remover os 2 primeiros caracteres, retornando só a palavra"""
    word = word[2:]  
    
    return word.upper()



STATUS = [
    r"""
_____________
|            |
|            
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|            |
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           / 
|=====================
""",
    r"""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
''''''''''|_`-' `-' |'''|
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
VOCÊ PERDEU, NOOB!
"""
]