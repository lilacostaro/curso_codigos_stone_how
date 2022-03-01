"""
How Bootcamps - Stone - /código[s]
Data: 01/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 6:

Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] 
A saída deve ser:
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]
"""
# Definindo a lista
lista = ['Olá', '', 'meu', 'nome', '', 'é', 'Camila', '', 'e', '', 'estou', '', 'estudando', '', 'Python'] 

# Definindo o loop pra varer todos os elementos da lista
for i in lista:
    # Definindo a condição
    if i == '':
        # Excluindo os elementos que atendem a condição
        lista.pop(lista.index(i))
        
# Imprimindo o resultado
print(f'\n{lista}\n')

# Bonus
# Imprimido a lista como frase
print(' '.join(lista))