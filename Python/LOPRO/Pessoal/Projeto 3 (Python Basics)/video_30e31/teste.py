"""
a)Faça um programa que peça ao usuario para digitar um numero inteiro, informe se este numero é par ou impar.
Caso o usuario nao digite um numero inteiro, informe que nao é um numero inteiro
-
b)Faça um prgrama que pergunte a hora ao user e, baseando-se no horario descrito, exiba a saudação apropriada,
Ex: bom dia se for de dia, boa tarde se for de tarde, boa noite se for de noite
-
c)Façã um programa que peça o primeiro nome do user.
Se o nome tiver 4 letras ou menos escreva "seu nome é mt curto", se tiver entre 5 e 6 letras, escreva, "seu nome é normal"
, maior que 6 escreva "seu nome é mto grande"
"""

userint = input('Qual numero deseja checar: ')
if userint.isnumeric():
    userint = int(userint)
    if int(userint) % 2 == 0:
        print('O numero', userint, 'é par!')
    else:
        print(f'O numero {userint} é impar!')
else:
    print('Digite um numero inteiro')
"""
Checagem invertida:
userint = input('Qual numero deseja checar: ')
if not userint.isnumeric():
    print('Isso nao é um numero inteiro')
else:
    userint = int(userint)
    if not userint % 2 == 0:
        print('O numero', userint, 'é impar!')
    else:
        print(f'O numero {userint} é par!')
"""
print()
horasuser = input('Quantas horas são (entre 0 e 23): ')
if horasuser.isnumeric():
    horasuser = int(horasuser)
    if 0 <= horasuser <= 11:
        print('Agora são', horasuser, 'horas, Bom dia!')
    elif 12 <= horasuser <= 17:
        print(f'Agora são {horasuser} horas, Boa tarde!')
    elif 18 <= horasuser <= 23:
        print('Agora são', horasuser, 'horas, Boa noite!')
else:
    print('Digite um horario entre 0 e 23')
print()
nomeuser = input('Seu nome: ')
if nomeuser.isalpha():
    letrasnomeuser = len(nomeuser)
    if letrasnomeuser <= 4:
        print('Seu nome é curto!')
    elif len(nomeuser) == 5 or len(nomeuser) == 6:
        print('Seu nome é normal!')
    elif len(nomeuser) > 6:
        print('Seu nome é gigantesco!')
