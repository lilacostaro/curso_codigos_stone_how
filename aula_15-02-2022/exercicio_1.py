"""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Camila Rodrigues Costa
Descrição: Codigo proposto pelo instrutor Henrique Junqueira na primeira aula do bootcamp.
O código recebe os valores de distancia e velocidade média do usúario e retorna o tempo estimado da viagem com duas casas decimais.
"""

# print('Hello World!')

distancia = float(input('Digite a distancia em Km: '))

velocidade_media = float(input('Digite a velocidade média em Km/h: '))

tempo_total_horas = distancia / velocidade_media

print(f'\nO tempo estimado é de {tempo_total_horas:.2} horas\n')