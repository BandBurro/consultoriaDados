"""
Condicional OR
"""
nome = input()
"""
if nome:
    print(nome)
else:
    print('Voce nao digitou nada')
"""
print(nome or 'voce nao digotou nada')  # se nome for V, printe ele, caso nao, printe a segunda STR
"""
Posso continuar colocando mais condições com mais "ors"
"""
print(
    nome or None or False or 0 or 'voce nao digotou nada' or 'Fodase')  # se nome for V, printe ele, caso nao, printe a segunda STR
"""
A primeira condição que for cumprida, vai ser executada e ignorar o resto
"""
a = 0
b = None
c = False
d = []
e = {}  # Dicíonario
f = 22
g = 'Luiz'
variavel = a or b or c or d or e or f or g  # Posso colocar a ordem que eu quiser
print(variavel)  # Printa a variavel 'f' pois é a primeira que retorna V

if a:
    variavel = a
elif b:
    variavel = b




