"""
A lista é um tipo de dado, assim como os dados primitivos (str, int, float, bool), a diferença é que a lista pode conter
varios valores dentro de [colchetes] de varios tipos, tipo [1, 2, 3, 4, 'Eu', True]
Fatiamento (quando usa-se os colchetes [])
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4
lista = ['a', 'b', 'c', 'd', 'e']  # Para acessar estes valores, eu uso indices
#        -5   -4   -3   -2   -1
print(lista[1])
print()
str = 'abcde'  # Para acessar um dos valores, basta printar o indice da str
print(str[1])  # Poderia colocar qualquer outro numero de 0 a 5
print()
""" variavel str, é que na variavel lista eu posso ter varias coisas dentro
de um so indice, ate uma str inteira por
A grande diferença entre a variavel lista e a exemplo lista = ['a', 'bacana', 'carne', 'd', 'e']
"""
lista2 = ['a', 'bacana', 'cana', 3, 'e', 9.78]
print(lista2[3])
print(lista2[2])
print(lista2)  # Posso printar ate a lista inteira
print()
"""
Caso eu queria modificar um indice especifico da lista, posso isolar o indice como variavel
"""
lista2[4] = 'fodase'
print(lista2[4])
print()
"""
As listas, assim como as str, tambem suportam o fatiamento no formato de range
"""
lista2 = ['a', 'bacana', 'cana', 3, 'e']
print(lista2[0:3])  # O numero que para nao é incluido
print(lista2[0:4])  # Ou print(lista2[:4]), ao omitir, presume-se o 0
print(lista2[::2])  # Ou print(lista2[0:0:2])
print(lista2[::-1])  # Esse metodo inverte a ordem da lista, bom macete
print()
"""
Extend = EXTENDE as listas / variaveis, funciona de um jeito parecido com concatenar str
Append = ADICIONA um valor no FINAL da lista, inclusive, sendo um indice a mais
Insert = "EMPURRA" a lista para frente, colocando o valor inserido no indice indicado
Pop = DELETA um valor no FINAL da lista
Del = DELETA uma fatia de uma lista (usando os colchetes [1:3], isso é, do 1 ao 2, pq nao conta o ultimo)
Min Max = Pega o Minimo (menor indice) e Maximo (maior indice) de uma coisa iteravel
Range = 
list = CONVERTE um objeto iteravel em uma lista com list, como o exemplo, list(range(1,10))
"""
print('Extend')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)
print()
l1.extend(l2)  # Uma forma de fzer "l3 = l1 + l2" sem precisar de uma nova variavel, muda-se o valor da variavel apartir deste ponto
print(l1)
l1.extend('a')  # Posso adicionar qualquer coisa
print(l1)
print()
# Append
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)
l2.append('b')  # Append insere um novo valor no FINAL da lista, adicionando um indice
l2.append(l1)
print(l2)
print()
# Insert
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)
l2.insert(2, 'banana')  # "Empurra" a lista para frente, colocando o valor inserido no indice indicado, portanto, banana vai passar a ser o indice 2 e indice seguinte, o proximo
print(l2)
print()
# Pop
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)
l2.insert(2, 'banana')
print(l2)
l2.pop()
print(l2)
print()
# Del
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Mind os indices
print(l1)
del(l1[3:5])  # Deleta uma fatia de uma lista, os valores indicados sao os indices de 3 a 5, lembre-se que o ultimo nao é incluso
print(l1)
l1.insert(0, 'banana')
print(l1)
del(l1[0])  # posso tambem deletar uma coisa em específica
print(l1)
# Max Min
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l1))
print(min(l1))
print()
# Range
l1 = range(1, 10)
print(l1)
# Converter objeto iteravel em uma lista com list
l1 = list(range(1, 100))  # Pula o ultimo valor
print(l1)
l1 = list(range(0, 100, 5))  # Posso tambem adicionar um valor final para pular, como de costume de uma função range
print(l1)
print()
# Exemplos
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Ou, list(range(1,10))
soma = 0
for valor in l1:
    print(valor)
    soma += valor  # A cada iteração do laço for, soma-se o valor ao anterior, debugg para ver
print(soma)
print()
l1 = ['Str', True, 10, -20.5]
for elem in l1:
    print(f'O tipo de {elem} é {type(elem)}')
print()
# Jogo tipo forca
secret = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Perdeu!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhhh, isso nao vale, digite apenas UMA letra.')
        continue
    digitadas.append(letra)  # Adiciona o Input valido, pois tem que passar pelo if acima, à lista no inicio do jogo
    print(digitadas)
    if letra in secret:
        print(f'Acertou uma, hehe, a letra {letra} faz parte da palavra')
    else:
        print(f'Welp, a letra "{letra.upper()}" não ta na palavra')
    secreto_temporario = ''
    for letra_secreta in secret:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta  # Duas strings se concatenam
        else:
            secreto_temporario += '*'
    if secreto_temporario == secret:
        print('Boa, acertou miseravi')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secret:
        chances -= 1
    print(f'Vc ainda tem {chances} chances')
    print()




