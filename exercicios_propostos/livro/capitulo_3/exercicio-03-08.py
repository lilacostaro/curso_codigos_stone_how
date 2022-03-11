"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python

Exercício 03-08: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

OBS: 1m = 100cm
     1cm = 10mm 
     logo 1m = 1000mm
"""
# Recebendo o valor em metros
metros = float(input('Digite o comprimento em metros: '))

mm = int(metros * 1000)

print(f'{metros} metros correspondem a {mm} milimetros.')