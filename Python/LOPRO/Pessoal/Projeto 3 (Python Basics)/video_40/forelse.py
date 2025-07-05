"""
For / Else
For tambem tem break e continue
Raramente usado, assim como o whileelse
"""

variavel = ['asdas', 'fdadsg', 'aJsdsada']
for valor in variavel:
    print(valor)
    continue  # Se nao fosse o continue, ele printaria duas vezes a lista, mas como o continue leva o PC pro laço FOR novamente, ele ignora o print debaixo
    print(valor)
print()
for i in variavel:
    if i.startswith('J'):  # essa operação checa se a variavel começa com o que pediu, apenas com STR
        print('Começa com J')  #  O pyton vai fazer diferenciação entre J e j,
    else:
        print('Nao começa com J')
print()

comecacomj = False
for ii in variavel:
    if ii.lower().startswith('j'):  # O pyton vai fazer diferenciação entre J e j, por isso usa o .lower()
        comecacomj = True  # Consigo mudar o valor de uma variavel no "meio do caminho" se condicionar tal função

if comecacomj:
    print('Existe uma palavra que começa com J')
else:
    print('Nao exist nada que começa com J')
print()
# Tambem posso escrever o codigo de cima de uma maneira mais enxuta e clara desse jeito
for ii in variavel:
    if ii.lower().startswith('j'):
        break
else:
    print('Nao exist nada que começa com J')


