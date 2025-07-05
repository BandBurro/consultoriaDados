'''
IF, ELIF e ELSE
Condicionais booleanos
if
    elif
    else
'''
#if False:
    #print("V")
#else:
    #print(f'A minha expressao nao é verdadeira')
"""
Hierarquia entre os codigos, tudo que tem os 4 espaços antes estao condicionados ao valor superior
"""
idade = input('Qual a sua idade?: ')
maioridade = int(idade) >= 18
if maioridade:
    print('Digite seu nome abaixo')
    print()
    nomeuser = input('')
    if 'n' in nomeuser:
        print('Seu nome tem N')
    else:
       print('Seu nome nao tem N')
elif maioridade <= 17:
    print('Menor de idade')

"""
if False:
    print("V")
    print(f'teste 2')
elif True:
    print('Agora é verdadeiro')
    nome = input(f'qual seu nome? ')
    print(f'Seu nome é {nome}')
'''
O if é uma condicional que trabalha com valores booleanos por padrao, ela sempre será executada caso seja um true
e nao sera executada caso seja um false
'''
elif True:
    print(f'Mais uma vdd')
    print(22+22)
else:  # Caso eu tire esse else, nada sera executado, pois tudo sera falso
    print('A minha expressao nao é verdadeira')
    print('Ola')
"""
"""
uso um elif para cada coisa que eu quiser verificar antes de me dar o resultado
a ordem dos elif vao se respeitados, so verifica um se o de cima nao tiver
O else so sera executado se todos os elif forem falsos
"""

