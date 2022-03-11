"""
How Bootcamps - Stone - /código[s]
Data: 18/02/2022
Autor: Camila Rodrigues Costa
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Parte do livro Introdução à Programação com Python
Exercício 02-02: Converta uma expressão matemática no interpretador
Digite a seguinte expressão no interpretador:
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das operações é importante.
"""

x = 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2

"""
O resultado da expressão é 81.0

No papel primeiro fariamos:
10 ** 2 = 100 e a expressão ficaria:
10 % 3 * 100 + 1 - 10 * 4 / 2
Agora a prioridade é das divisoes e multiplicações na ordem em que aparecem:
10 % 3 = 1 uma vez que queremos o resto
10 * 4 = 40
Agora temos:
1 * 100 + 1 - 40 / 2
Agora fazemos:
1 * 100 = 100
40 / 2 = 20
E temos:
100 + 1 - 20
Total = 81

Obs: No interpretador o resultado é 81.0 por que toda divisão em Python retorna um float.
"""