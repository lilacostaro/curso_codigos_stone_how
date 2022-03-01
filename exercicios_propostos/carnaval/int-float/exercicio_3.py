"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: tipos numéricos
Diversão do carnaval \o/

Exercício 3:

No exercício acima você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.

Dica!
A área de um triângulo também é dada pela seguintes fórmulas abaixo
s = ( s1 + s2 + s3) / 2
area=√(s.(s-s1).(s-s2).(s-s3))

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

"""
# Recebendo o input do usuario
lado_1 = int(input("Digite o valor do primeiro lado to triangulo: "))
lado_2 = int(input("Digite o valor do segundo lado to triangulo: "))
lado_3 = int(input("Digite o valor do terceiro lado to triangulo: "))

# Checando a existencia do triangulo
if ((abs(lado_2 - lado_3) < lado_1 < (lado_2 + lado_3)) and 
    (abs(lado_1 - lado_3) < lado_2 < (lado_1 + lado_3)) and 
    (abs(lado_1 - lado_3) < lado_2 < (lado_1 + lado_3))):
    s = ( lado_1 + lado_2 + lado_3) / 2
    area = (s * (s - lado_1) * (s - lado_2) * (s - lado_3)) * (1/2)
else:
    area = 'O triangulo não existe'
    
print(f'A área do triango composto pelos lados {lado_1}, {lado_2} e {lado_3} é: {area}')
    

















