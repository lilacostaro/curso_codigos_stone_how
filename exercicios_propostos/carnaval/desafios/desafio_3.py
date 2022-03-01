"""
# Questão 03

Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.
"""

# define a função numero_anagramas que recebe como parametro a palavra fornecida
def numero_anagramas(palavra):
    """
    Parte 1: Retorna todas as substrings da palavra
    """
    # lista vazia que ira receber as substrings da palavra
    lista = []
    
    # variavel que recebe o numero de anagramas na palavra
    qtd_anagramas = 0
    
    # lista que recebe os anagramas da palavra. 
    dict_anagramas = []
    
    # variavel que recebe a quantidade de caracteres na palavra
    palavra_size = len(palavra)
    
    # Loop exterior que determina o primeiro parametro do slice da palavra
    for j in range(palavra_size):
        
        # Loop interior que determina o segundo parametro do slice da palavra
        for i in range(1, palavra_size+1):
            
            # Retorna todas as substrings da palavra, incluindo a mesma, e adiciona a lista
            substrings = palavra[j:i]
            # Condição para não adicionar strings vazias a lista 
            if substrings:
                lista.append(substrings)         
    
    """
    Parte 2: Compara todas as substrings da palavra para determinar se existem 
    anagamas e quais são eles.
    Nesta parte do código, temos um loop exterior e um interior, o loop exterior gera um dicionario
    que será comparado com todos os dicionarios do loop interior, para determinar se são iguais,
    caso sejam, o valor da variavel 'qtd_anagramas' e a lista 'dict_anagramas' seram atualizados.
    Uma vez que todas as substrings do loop interior tenham sido comparadas com a primeira substring da lista,
    o loop exterior ira gerar um dict para a proxima substring e compara-lá com todas as substrings do loop interior,
    que pega todas as substrings da lista, que vem depois da substring utilizada pelo loop  exterior.
    E isso se repete até o loop exterior percorrer todas as substrings da lista, com excessão da ultima.
    """
    # Retorna a quantidade de substrings na lista
    lista_size = len(lista)
        
    # Loop externo para converter as substrings em dicionario
    # que recebe o caractere como chave e a quantidade de vezes que ele aparece como valor.
    for l in range(lista_size):
        # dicionario vazio que ira receber as informações da substring
        dict_1 = {}
        # selecionando a substring
        nome1 = lista[l]
        
        # Para cada repetição do caractere, será adicionado 1 ao seu valor. 
        # Se o caractere não se repetir, o valor default é 1 
        for letra in nome1:
            try:
                dict_1[letra] = dict_1[letra] + 1
            except:
                dict_1[letra] = 1
           
        # Loop interno para converter as substrings em dicionario
        # que recebe o caractere como chave e a quantidade de vezes que ele aparece como valor.   
        for i in range(l+1, lista_size):
            # dicionario vazio que ira receber as informações da substring
            dict_2 = {}
            # selecionando a substring
            nome2 = lista[i]
            
            # Para cada repetição do caractere, será adicionado 1 ao seu valor. 
            # Se o caractere não se repetir, o valor default é 1 
            for letra in nome2:
                try:
                    dict_2[letra] = dict_2[letra] + 1
                except:
                    dict_2[letra] = 1
            
            # Operação que determina se os dicionarios são iguais, e portanto se as substrings são anagramas
            anagrama = dict_1 == dict_2
            
            # Caso as substrings sejam anagramas, o valor da variavel 'qtd_anagramas' e a lista 'dict_anagramas' serão atualizados
            if anagrama == True:
                # soma um ao valor de 'qtd_anagramas' toda vez que a variavel 'anagrama' retorna True
                qtd_anagramas = qtd_anagramas + 1
                # Cria uma lista com as substrings que são anagrama
                lista_anagramas = [nome1, nome2]
                # adiciona a os valores da lista 'lista_anagramas' a lista 'dict_anagramas' 
                dict_anagramas.append(lista_anagramas)
            
            
    # Imprime a palavra que está sendo analisada
    print(f"\nA palavra é '{palavra}'")
    # Imprime a quantidade de anagramas presente na palavra
    print(f'Ela contém {qtd_anagramas} anagramas.')
    # Imprime os anagramas contidos na palavra
    print(f'Eles são:\n{dict_anagramas}\n')


# Testes unitarios    
if __name__=='__main__':     
    numero_anagramas('ovo')
    numero_anagramas('ifailuhkqq')
    numero_anagramas('maça')
    numero_anagramas('bolo')
    numero_anagramas('kamizaze')
    numero_anagramas('Python')








