# Positivos  [0123456789] cada um desses numeros é um !INDICE! de cada letra abaixo
texto      = 'Python fds'
# Negativos -[10987654321]
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