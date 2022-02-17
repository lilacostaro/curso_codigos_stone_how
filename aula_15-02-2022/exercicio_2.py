"""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Camila Rodrigues Costa
Descrição: Adaptação do codigo proposto pelo instrutor Henrique Junqueira na primeira aula do bootcamp.
Nesta versão, o usuario fornecerá o valor da diaria do carro e do adicional por Km rodado, 
uma vez que esse valor varia de acordo com o modelo do carro.
O usuario tambem fornecerá as datas de retirada e entrega do carro, e a quantidade de Km percorridos.
Com essas informaçoes o programa converte as datas para o formato de datetime, subtrai as data e retorna a quantidade de dias.
Então calcula o valor do aluguel do carro, o valor a ser pago por Km percorridos e o valor total a ser pago.
Devolvendo o valor com até 7 digitos, e duas casas decimais.
"""
from datetime import datetime

# Recebe os valores do usuario
preco_por_dia = float(input('Digite o valor diario do aluguel do carro: '))
preco_por_km = float(input('Digite o valor adicional por Km rodados: '))
data_inicial_text = input('Digite a data inicial no formato = dd/mm/aaaa: ')
data_final_text = input('Digite a data final no formato = dd/mm/aaaa: ')
qtd_km = int(input('Digite a quantidade de quilometros percorridos: '))

# Converte a data recebida em string para datetime
data_inicial = datetime.strptime(data_inicial_text, '%d/%m/%Y')
data_final = datetime.strptime(data_final_text, '%d/%m/%Y')

# Calcula a quantidade de dias do aluguel do carro
qtd_dias = data_final - data_inicial
qtd_dias = qtd_dias.days

# Calcula o valor a ser pago
preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia
preco_a_pagar = preco_total_km + preco_total_dia

# Retorna o valor final

print(f"\nTotal a pagar: R$ {preco_a_pagar:7.2f}")