# Iterar é passar por cada um dos elementos de uma str, um elemento precisa ser iteravel para isso, precisa ter indices, por exemplo
#         Indices
#        0123456789......................33, esta STR tem 34 elementos, pq conta-se o 0

frase = 'o rato roeu a roupa do rei de roma'
tamanhofrase = len(frase)  # Lembrando que o len me retorna um int
print(len(frase))
contador = 0
frasenova = ''
inputdeletra = input('Qual a letra deseja adicionar? ')

"""
print(frase[5]), posso trocar o valor do indice para um contador que loopéia um += ate o final da str
Como o contador passar por varios numeros, posso trocar o numero de indices para que as letras sejam reproduzidas
"""

while contador < len(frase):  # Tambem posso usar direto a variavel tamanhofrase
    print(frase[contador], contador)
    letra = frase[contador]  # Neste caso é concatenação e nao soma, pois trabalha-se com str
    if letra == inputdeletra:
        frasenova += inputdeletra.upper()  # Esta função converte a letra para maiusculo
else:
    frasenova += letra
    print(frasenova)
    contador += 1

print(frasenova, 'asd')








