"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e Sets
Diversão do carnaval \o/

Exercício 2:

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. 
Exemplo:
>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.
"""
# Definindo o dicionario
estados = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }

# Recebendo o input do usuario
sigla = input('Digite a sigla que deseja consultar: ').upper()

# verificando se a sigla corresponde a um estado e imprimindo o resultado
if sigla in estados.keys():
    print(f'\nO nome completo do estado é {estados[sigla]}')
else:
    print('\nSigla não corresponde a um estado brasileiro')






