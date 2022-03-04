"""
How Bootcamps - Stone - /código[s]
Data: 28/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 5:

Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira 
(no formato antigo) com três letras, um traço e quatro números. Exemplos: 
    
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, 
o programa deverá exibir False 
"""
# Recebendo as informaçoes da placa
placa = input('Digite uma placa: ').upper()
# Definindo uma lista com todos os numero e outra com todas as letras
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'W', 'Y']

# Checando cada elemento da string 
if ((placa[0] in alf) and (placa[1] in alf) and (placa[2] in alf) and (placa[3] == '-') 
    and (placa[4] in numeros) and (placa[5] in numeros) and (placa[6] in numeros) and 
    (placa[7] in numeros)):
    print('True')
else:
    print('False')
