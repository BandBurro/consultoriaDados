strg = 'o brasil é o pais do futebol, o brasil é o penta.'
lista_1 = strg.split(
    ' ')  # Pega todos os termos dividos pelo item que coloca dentro do split e faz uma lista como nos dois prints abaixo
lista_2 = strg.split(',')
for valor in lista_1:
    print(
        f'{valor}    {lista_1.count(valor)}')  # Conta quantas vezes cada valor de iteração apareceu na frase, diferencia os maiusculos e minuculos, conta varias vzes o 'o' pois este é iterado varias vezes
print()
"""
Teste o print sem o termo {valor}, este retornara apenas o numero seco de vezes que cada termo apareceu sem dizer qual foi
for valor in lista_1:
    print(
        f'{}    {lista_1.count(valor)}')
"""
for valor in lista_2:  # Este codigo foi usado la em cima para exemplificar o split por vigula
    print(valor.strip().capitalize())
print()

for indice, valor in enumerate(lista_1):  # esses dois valores (indice e valor) é o ato de desempacotar uma lista, o primeiro numero me da o indice e a outra me da o valor real iterado
    print(indice, valor, lista_1[indice])
print()

