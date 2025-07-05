'''
While Else
contadores e acumuladores

'''
"""
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1

# Debug e step over para o passo a passo da operação
"""
"""
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')
"""
"""
Tambem é possivel usar o else no laço while, o else vai ser um "entao" para o momento em que o while seja Falso
É extremamente similar a voce simplesmente printar um "print('cheguei no else')" no final do codigo, mas nao é a mesma coisa
pois caso eu saia do laço antes da expressao principal ser Falsa, como por exemplo, dando um break, o else nao será executado
"""

contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')  # Este nao foi executado por ser uma exeção ao while, como o print abaixo nao depende do while, ta tudo certo
print('Isso sera executado')  # O print do else, PRECISA QUE O WHILE SEJA F para ser executado, esta que é a grande diferença

