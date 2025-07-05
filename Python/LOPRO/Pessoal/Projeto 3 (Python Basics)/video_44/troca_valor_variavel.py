"""
Como inverter os valores de variaveis
"""
x = 10
y = 'Luiz'
"""
E se eu quiser inverter o x e o y, no caso, x = 'Luiz' e y = 10?
"""
z = x  # Este z serviria de sustentação para o valor da variavel X
x = y
y = z
print(f'x = {x}, y = {y}')
"""
Este seria o metodo mais comum na maioria das linguagens de programação, mas no python, ha outro jeito bem mais simples
"""
x = 10
y = 'Luiz'
x, y = y, x
print(f'x = {x}, y = {y}')
"""
Com mais valores
"""
x = 10
y = 'Luiz'
z = 'Eu'
x, y, z = z, x, y
print(f'x = {x}, y = {y} e z = {z}')






