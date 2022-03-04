"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 3:

A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho	             Nível sonoro (dB)
Britadeira	         130
Cortador de grama	 106
Despertador	         70
Cômodo em silêncio	 40


Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo.
"""
# Recebendo o valor do usúario
db = int(input('Digite o valor dos decibeis: '))

# definindo o dicionario com as informações da tabela
tabela = {'Britadeira': 130, 'Cortador de Grama': 106, 'Despertador': 70, 'Cômodo em silêncio': 40}
# Criando uma tabela apenas com as chaves
tabela_keys = list(tabela.keys())

# Checando se o valor corresponde a um valor na tabela
if db in tabela.values():
    for key, value in tabela.items():
        if db == value:
            print(f'\nEsse valor de decibeis corresponde a: {key}')
# Deteminando as demais condições
elif db > 130:
    print(f'\nO valor esta acima do valor maximo da tabela!')
elif db > 106:
    print(f'\nO valor em decibeis esta entre {tabela_keys[1]} e {tabela_keys[0]}')
elif db > 70:
    print(f'\nO valor em decibeis esta entre {tabela_keys[2]} e {tabela_keys[1]}')
elif db > 40:
    print(f'\nO valor em decibeis esta entre {tabela_keys[3]} e {tabela_keys[2]}')
else:
    print(f'\nO valor está abaixo dos valores na tabela!')
    