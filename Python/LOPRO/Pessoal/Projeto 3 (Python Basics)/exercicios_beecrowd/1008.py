"""
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora
 e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de
horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igual
dade. No caso do salário, também deve haver um espaço em branco após o $.
"""
"""
user = input('Número do funcionario: ')
horas = int(input('Horas trabalhadas: '))
valor = float(input('Valor por hora: '))
resultado = horas * valor
f25 = 25
f1 = 1
f6 = 6
hf25 = 100
hf1 = 200
hf6 = 145
phf25 = 5.50
phf1 = 20.50
phf6 = 15.55
sf25 = hf25 * phf25
sf1 = hf1 * phf1
sf6 = hf6 * phf6
# print()
# print(sf25)
# print(sf1)
# print(sf6)
# print('O funcionário', user,'recebera', resultado)
# print('O funcionario', user, 'trabalhou', horas, 'horas no valor de', valor, 'e recebera', resultado)
print('Number = ', user)
print(f'Salary = U$ {resultado:.2f}')
"""

user = int(input('Número do funcionario: '))
horas = int(input('Horas trabalhadas: '))
valor = float(input('Valor por hora: '))
resultado = horas * valor
print()
if user != 25 and user != 1 and user != 6:
    print('Você Não Existe')
else:
    print('Você é', user)
    print(f'Salary = U$ {resultado:.2f}')