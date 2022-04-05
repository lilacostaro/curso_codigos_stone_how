"""
How Bootcamps - Stone - /código[s]
Data: 22/03/2022
Autor: Camila Rodrigues Costa
Descrição: Modulos Built-In
"""
from math import radians, acos, cos, sin  

t1, g1 = map(float, (input("Digite as coordenadas do primeiro ponto separado por virgula: ")).split(","))
t2, g2 = map(float, (input("Digite as coordenadas do segundo ponto separado por virgula: ")).split(","))

t1, g1, t2, g2 = radians(t1), radians(g1), radians(t2), radians(g2)

distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
distancia_mi = distancia * 0.621371

print(f'A distancia calculada em Km é: {distancia:.2f} e em milhas é {distancia_mi:.2f}')

# -20.8480435, -49.3872444
# -25.4947402, -49.7298817

# Distância total: 9.477,61 km (5.889,11 mi)
# 51.32773944557195, -0.1583631915949022
# -23.527914263327546, -46.65250311176724
