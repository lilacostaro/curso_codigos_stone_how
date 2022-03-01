"""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Camila Rodrigues Costa
Descrição: Introdução a sintaxe e tipos de dados

Dica da Tia Fer: Imaginem que temos um objeto pessoa. 
Atributo é um valor que esse objeto armazena e método é uma ação que esse objeto executa. 
Por exemplo, o objeto pessoa pode ter o atributo nome com o valor "Fernanda Hembecker" armazenado (pessoa.nome = "Fernanda Hembecker"). 
Eu posso codificar um método retornar_nome( ) que retorna o valor do atributo nome. 
Se combinar com um print, poderia apresentar valor do atributo nome do objeto pessoa na tela: print(f"Nome: {pessoa.retornar_nome()")

"""

nome = 'Camila Rodrigues Costa'

letra = 'o'

print(f'Meu nome é {nome.capitalize()}')
print(f'Meu nome é {nome.upper()}')
print(f'Meu nome contem {nome.count(letra)} letras {letra}')
print(f'Meu nome contem {len(nome)} letras.')
