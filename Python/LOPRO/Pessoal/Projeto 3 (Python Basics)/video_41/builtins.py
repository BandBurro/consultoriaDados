"""
Split - Divide uma str
Join - Junta uma lista
Enumerate - Enumerar objetos iteraveis
"""
# Split
strg = 'o brasil é o pais do futebol, o brasil é o penta.'
lista_1 = strg.split(
    ' ')  # Pega todos os termos dividos pelo item que coloca dentro do split e faz uma lista como nos dois prints abaixo
lista_2 = strg.split(',')
print(lista_1)
print(lista_2)
print()
for valor in lista_1:  # Aqui a cada espaço
    print(valor)
print()
for valor in lista_2:  # Aqui divide por vigula
    print(valor)
print()
for valor in lista_1:
    print(
        f'{valor}    {lista_1.count(valor)}')  # Conta quantas vezes cada valor de iteração apareceu na frase, diferencia os maiusculos e minuculos, conta varias vzes o 'o' pois este é iterado varias vezes
print()

contagem = 0
palavra = ''
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareu mais vezes é {palavra}, foi {contagem} vezes')
print()

contagem = 0
palavra = ''
for valor in lista_2:
    qtd_vezes = lista_2.count(
        valor)  # Neste caso, a lista 2 ta com o split por vírgula, por isso ficou assim, a lista 1 esta sendo separada por espaço, dando mais funcionalidade pro codigo
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareu mais vezes é {palavra}, foi {contagem} vezes')
print()
"""
Este codigo abaixo foi usado la em cima para exemplificar o split por vigula, mas é bom notar que o print seco dele
for valor in lista_2:
    print(valor)
Daria resultados ruins, o inicio da frase depois da virgula teria espaço e estaria minusculo, portanto, usa-se o strip
para comer todos os espaços do final e do inicio alem da capitalize para deixar a primeira letra maiuscula de todos
os valores da lista_2 splitada por virgula
"""
for valor in lista_2:  # Este codigo foi usado la em cima para exemplificar o split por vigula
    print(valor.strip().capitalize())
print()

# O join pega todos os elementos de uma lista e torna em uma str inteira, é quase o inverso do split
listajoin = ['o', 'brasil', 'é', 'penta']
str_1 = 'o brasil é o pais do futebol'
print(str_1.split(' '))
str_2 = ' '.join(listajoin)  # Coloco em str o termo que eu quero usar para juntar os termos da lista em um join, no caso, usarei o espaço, ou seja, apenas uma str vazia
print(str_2)
print()

for indice, valor in enumerate(
        listajoin):  # esses dois valores (indice e valor) é o ato de desempacotar uma lista, o primeiro numero me da o indice e a outra me da o valor real iterado
    print(indice, valor, listajoin[indice])
print()

# Listra dentro de lista
lista = [[1, 2], [3, 4], [5, 6], [7, 8]]
for valor in lista:
    print(valor[0], valor[1])
print()
lista = [[0, 'Luiz'], [1, 'Fodase'], [2, 'Maria'], [3, 'Dnv']]
for indice, nome in lista:  # A primeira variavel pega o primeiro valor da coluna, ou seja, algo entre 0 e 3, a segunda variavel, pega valores da segunda coluna, ou seja, os nomes, portanto, para desempacotar uma lista, preciso que esta lista tenha outras listas dentro
    print(indice, nome)  # Fez a mesma coisa que a função enumrate, mas a função enumrate faz com tuplas
print()
lista2 = ['Luiz', 'Fodase', 'Maria', 'Dnv']
for indice, nome in enumerate(lista2):  # A função enumrate me da uma "coluna fantasma" com o indice
    print(indice, nome)
    print()
"""
Tambem posso desempacotar os termos da lista diretamente por nomeação de variaveis
"""
v1, v2, v3, v4 = lista2
print(v3, v1)


