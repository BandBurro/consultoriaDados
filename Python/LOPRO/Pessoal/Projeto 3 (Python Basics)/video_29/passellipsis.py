#  Placeholders

valor = True
if valor:
    print('X')
else:
    print('Y')
"""
Caso eu queria deixar um lugar pronto para preencher volume, eu nao posso colocar apenas um comentario, pois ele crasharia, assim:
valor = True
if valor:
    #  Colocar tal coisa futuramente
else:
    print('Y')
Neste caso, usa-se o "pass" ou "..." (ellipsis), e assim o codigo continua sendo executado, obviamente, apenas a parte que foi colocada como
pass nao será executada
"""

valor = False
if valor:
    pass
else:
    print('Y')

valor = True
if valor:
    print('X')
else:
    ...

