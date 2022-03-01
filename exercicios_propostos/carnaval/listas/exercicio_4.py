"""
How Bootcamps - Stone - /código[s]
Data: 01/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 4:

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas 
as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 
Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho
"""
# Definindo a lista dos meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Definindo a lista de temperaturas
temp_lista = []

# Recebendo input do usuario
for i in meses:
    temp_lista.append(float(input(f'Digite a temperatura do mês de {i}: ')))

# Definindo a media    
media = sum(temp_lista) / len(temp_lista)

# Imprimindo o valor da média anual
print(f'\nMeses com temperatura acima da média anual de {media:.1f}°C:')

# Declarando um looping para varer toda a lista de temperaturas
for temperatura in temp_lista:
    # Definindo a condição
    if temperatura > media:
        # Imprimindo as temperaturas e o mes correspondente que obdecem a condição
        print(f'\n{temperatura} - {meses[temp_lista.index(temperatura)]}')
    

    
    