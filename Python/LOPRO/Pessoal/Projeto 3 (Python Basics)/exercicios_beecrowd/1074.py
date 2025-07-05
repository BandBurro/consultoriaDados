# Feito
"""
usern = input('Numero de testes (N) que seja < 20000: ')
x = -10000
y = 10000
acumuladora = 0

if usern.isnumeric():
    usern = int(usern)
    while x < y:
        x += 1
        if x > 0 and x % 2 == 0:
            print(x, 'EVEN POSITIVE')
        elif x > 0 and x % 2 != 0:
            print(x, 'ODD POSITIVE')
        elif x < 0 and x % 2 == 0:
            print(x, 'EVEN NEGATIVE')
        elif x < 0 and x % 2 != 0:
            print(x, 'ODD NEGATIVE')
        elif x == 0:
            print(x, 'NULL')
        acumuladora += 1
        if acumuladora == usern:
            break
"""
# Com for
n1 = int(input())
n2 = int(input())
stopper = 0
casos = range(n1, 10001)
limites = range(n2, 10001)
if n1 < 0:
    print('Digite um numero maior que 0 e menor que 10000')
if -10000 < n2 > 10000:
    print('Digite um numero maior que -10000 e menor que 10000')
for numero1 in limites:
    stopper += 1
    if numero1 % 2 == 0 and numero1 >= 0:
        print(f'{numero1} é par e postivo')
    elif numero1 % 2 != 0 and numero1 > 0:
        print(f'{numero1} é impar e positivo')
    elif numero1 % 2 != 0 and numero1 < 0:
        print(f'{numero1} é impar e negativo')
    elif numero1 % 2 == 0 and numero1 < 0:
        print(f'{numero1} é par e negativo')
    elif numero1 == 0:
        print(f'{numero1} é par e postivo')
    if stopper == n1:
        break







