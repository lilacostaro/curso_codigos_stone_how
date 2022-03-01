"""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Autor: Camila Rodrigues Costa
Descrição: Estrutura condicional (if, elif, else)
"""
aluno = 'Camila Costa'

notas = []

notas.append(float(input('Digite a primeira nota: ')))

notas.append(float(input('Digite a segunda nota: ')))

notas.append(float(input('Digite a terceira nota: ')))

nota_media = sum(notas) / len(notas)

nota_minima_aprovacao = 7
nota_minima_rec = 5

if (nota_media >= nota_minima_aprovacao) and ('Camila' in aluno):
    status = 'aprovado(a)'
    nota_media = 10
elif (nota_media >= nota_minima_aprovacao):
    status = 'aprovado(a)'
elif nota_media >= nota_minima_rec:
    #Qual é a nota minima?
    notas.sort()
    print(notas)
    notas.pop(0)
    print(notas)
    status = 'em recureração'
else:
    status = 'reprovado(a)'
    
nota_media_arred = round(nota_media, 2)

print(f'\nA média do(a) aluna(a) {aluno} é {nota_media_arred} e ele(a) está {status}!')