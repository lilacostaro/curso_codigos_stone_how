"""
How Bootcamps - Stone - /código[s]
Data: 01/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 7:

Dada a lista de strings [“1”, “7”, “99”, “15”] 
construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, 
converta todos os elementos para str.
"""
# Definindo a lista
lista = ['1', '7', '99', '15']

print(f'\nLista original: {lista}')

# Convertendo os elementos para int
for i,j in enumerate(lista):
    lista[i] = int(j)
    
print(f'\nLista como Inteiro: {lista}')
      
# Convertendo de volta para string
for i,j in enumerate((lista)):
    lista[i] = str(j)
    
print(f'\nLista como string: {lista}')