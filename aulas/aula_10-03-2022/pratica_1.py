"""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Autor: Camila Rodrigues Costa
Descrição: Funções
"""
# definindo a função
# lst é um parametro do tipo lista
def calcula_media(lst: list) -> float:
    """Calcula a média aritmetica."""
    return sum(lst) / len(lst)

def calcula_media_ponderada(valores: list, pesos: list) -> float:
    """Calcula a média ponderada."""
    numerador = 0
    denominador = sum(pesos)
    for valor, peso in zip(valores, pesos):
        numerador = numerador + (valor * peso)
    return numerador / denominador

def pesos():
    # Perguntando ao usuario quantos alunos serão adicionados
    numero_alunos = int(input("Quantos alunos você irá digitar? "))
    # Perguntando para o usuario quantas notas serão digitadas por aluno
    numero_notas = int(input('Digite a quantidade de notas por aluno: '))

    pesos_notas = input('As notas terão pesos diferentes? sim[s] não[n] ').upper()
    
    if pesos_notas =='S':
        com_pesos(numero_alunos, numero_notas)
    elif pesos_notas =='N':
        sem_pesoss(numero_alunos, numero_notas)
        
def com_pesos(num_aluno, num_nota):
    alunos = {}
    nota_min = 7
    
    # Loop externo que ira pegar o nome do aluno
    for i in range(1, num_aluno+1):
        # declarando um lista vazia que receberá as notas
        notas = []
        pesos = []
        # Recebendo o nome do aluno
        nome = input(f'Digite o nome do {i}° aluno: ')
        # Loop inteno que receberá as notas
        for valor in range(1, num_nota+1):
            # Recebendo as noas
            nota = float(input(f'Digite a {valor}ª nota do {nome}: '))
            peso = int(input(f'Digite o peso para a {valor}ª nota: '))
            # Validando as notas, elas precisam estar entre 0 e 10
            while nota < 0 or nota > 10:
                # caso a nota não seja validada, outra nota sera requisitada
                nota = float(input('Nota fora do range, digite uma nota entre 0 e 1: '))
            # uma vez que a nota for validada, ela será adicionada a lista notas
            notas.append(nota)
            pesos.append(peso)
        # Uma vez que tudo for validado, o nome sera adicionado ao dicionario como chave e as notas como valor
        alunos[nome] = notas, pesos
        
    for aluno, notas in alunos.items():
            # Calculando a média de cada aluno
            media = calcula_media_ponderada(notas[0], notas[1])
            if media > nota_min:
                print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi aprovado!')
            else:
                print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi reprovado!')

def sem_pesos(num_aluno, num_nota):
    alunos = {}
    nota_min = 7
    
    # Loop externo que ira pegar o nome do aluno
    for i in range(1, num_aluno+1):
        # declarando um lista vazia que receberá as notas
        notas = []
        # Recebendo o nome do aluno
        nome = input(f'Digite o nome do {i}° aluno: ')
        # Loop inteno que receberá as notas
        for nota in range(1, num_nota+1):
            # Recebendo as noas
            nota = float(input(f'Digite a {nota}ª nota do {nome}: '))
            # Validando as notas, elas precisam estar entre 0 e 10
            while nota < 0 or nota > 10:
                # caso a nota não seja validada, outra nota sera requisitada                    nota = float(input('Nota fora do range, digite uma nota entre 0 e 1: '))
                # uma vez que a nota for validada, ela será adicionada a lista notas
                notas.append(nota)
        # Uma vez que tudo for validado, o nome sera adicionado ao dicionario como chave e as notas como valor
        alunos[nome] = notas
    
    for aluno, notas in alunos.items():
            # Calculando a média de cada aluno
            media = calcula_media(notas)
            if media > nota_min:
                print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi aprovado!')
            else:
                print(f'\nA media do aluno {aluno} foi {media:.2f}. E ele foi reprovado!')
    
        
                
if __name__ == '__main__':
    pesos()