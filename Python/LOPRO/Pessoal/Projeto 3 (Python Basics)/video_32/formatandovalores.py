"""
Formatando valores com modificadores

:s Texto (str)
:d Inteiros (int)
:f Números de ponto flutuante (float)
:.nf Quantidaed de casas decimais (float)
: (Caractere) (> ou < ou ^) Quantidade (Tipo - s, d ou f)

> Esquerda
< Direita
^ Centro
Sim, a esquerda e a direita sao invertidas, feiasso
"""

num1 = 10
num2 = 3
divisaonum1num2 = num1/num2
print(divisaonum1num2)  # Valor gigantesco
print('{}'.format(divisaonum1num2))  # Exatamente igual ode cima
print('{:.2f}'.format(divisaonum1num2))  # Limito o numero de casas decimais apenas dentro das chaves
#  Exatamente igual fazer print(f'{divisaonum1num2:.2f}')
'''
Tambem é possivel fazer type casting com estes comandos, como abaixo
'''
nome1 = 'Matheus'
nome2 = 2
print(f'{nome1:s}')  # Neste comando digo explicitamente para trata nome como str
print(f'{nome2:d}')  # Neste comando digo explicitamente para trata nome como int
print(f'{nome2:f}')  # Neste comando digo explicitamente para trata nome como float

num3 = 1
num4 = 1150
print(f'{num3:0>10}')
'''
Modificador de TAMANHO, pode ser usado em str, int ou float, preencho esse tamanho com o digito que eu qusier,
O numero que eu ponho dentro do comando é o numero TOTAL de casa, ou seja, vai contar 10 CONTANDO o numero que ja vai vir, no caso o numero 1
'''
print(f'{num4:0<5}')  # Caso eu coloque um numero MAIOR que o numero de casas que eu quero, aparecera apenas o numero da variavel
print(f'{num4:0^9}')  # Colocando um impar, a direita fica com o digito extra
print(f'{num4:#>10.2f}')  # Tambem é possivel fazer os comandos juntos
print(f'{num4:#<10.1f}')
print(f'{num4:#^10.1f}')

nome3 = 'asudhuidhfiojasuhiqw'
print((50-len(nome3))/2)
print(f'{nome3:#^50}')
nome4 = '{:@>50}'.format(nome3)
print(nome4)
nome5 = '{n:@>50}{n}{n}{n}{n}{n}'.format(n=nome3)  # Ou poderia nao dar um valor especifico pra nome3 e colocar 0's no lugar
print(nome5)
'''
O python tem um caralhada de função pra str, entao, nao tem como tratar de todas em video, o doc la tem o resto, preciso ver
Tem função que deixa tudo minusculo and so on
nome = matheus nepomuceno
nome.lower() tudo minusculo
nome.upper() tudo maisculo
nome.title() Primeiras Letras maisculas
'''







