userint = input('Qual numero deseja checar: ')
if userint.isnumeric():
    userint = int(userint)
    if int(userint) % 2 == 0:
        print('É par!')
    else:
        print('É impar!')
else:
    print('Digite um numero inteiro')
