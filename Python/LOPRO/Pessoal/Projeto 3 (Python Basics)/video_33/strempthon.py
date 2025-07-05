'''
Manipulando strs
- Str indicies
- Fatimaneto de str (inicio:fim:passo)
- Funçoes buil-in len,abs, type, print etc...
Essas funçoes podem ser usadas diretamente em cada tipo

Todas essas funções estao em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
'''
# Positivos  [0123456789] cada um desses numeros é um !INDICE! de cada letra abaixo
texto      = 'Python fds'
# Negativos -[10987654321]
print(texto[2])  # Aqui vou ver apenas o T
print(texto[5])  # Aqui vou ver apenas o N
print(texto[6])  # Aqui vou ver o spacebar
url = 'www.google.com.br/'
print(url[:-1])  # Isso se chama fatiamento, tirei apenas a barra /
novastr = texto[2:6]  # O ultimo caracter nao é incluido, portanto, devo colocar o seguinte caso queria acabar ali
print(novastr)
print(texto[0:6])
print(texto[:6])  # Caso nao coloque nada, ele vai presumir que começa do 0
print(texto[7:])  # Caso nao coloque nada, ele vai presumir que termina no ultimo indice
print(texto[-10])
print(texto[-10:-3])
print(texto[:-2])
"""
Tambem posso fazer pular caracteres
"""
print(texto[:6:2])  # Nesta estrutura, posso fazer um ultimo dois pontos para definir quais casas eu quero que ele leia, no caso, so de duas em duas
print(texto[:10:2])
print(texto[:10:5])
print(texto[0::5])
for letra in texto:
    print(letra)
