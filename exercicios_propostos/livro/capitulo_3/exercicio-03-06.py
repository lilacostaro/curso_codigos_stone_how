"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python
Exercício 03-06: Expressão para decidir se um aluno tem a média para passar de ano

Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: 
matéria1, matéria2 e matéria3.
"""
def aprovacao(m1, m2, m3):
    
    # Definindo a média
    media = 7
    
    # Definindo a condição
    if (m1 >= media) and (m2 >= media) and (m3 >= media):
        print('O aluno foi aprovado')
    else:
        print('O aluno não foi aprovado')
        

if __name__=='__main__':
    aprovacao(7, 8, 5)
    aprovacao(8, 7, 9)
    aprovacao(7, 7, 8)    