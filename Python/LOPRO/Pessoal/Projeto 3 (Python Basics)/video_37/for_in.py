"""
O for é o while mais preciso, com coisas finitas
Iterar sobre uma str, por exemplo, é feita com FOR e nao com while
"""

texto = 'Python'
c = 0

while c < len(texto):
    print(texto[c])  # O entre colchetes é um indexador
    c += 1
print()
"""
Evita-se o uso de while nesta situação justamente por finita, o while deixa a execução um pouco mais complexa do que
realmente precisa, necessitando de uma variavel acumuladora para definir o fim e iterar o texto inteiro
"""

texto = 'Python'
# Apesar de nao ter um contador, podemos colocar um com a função enumerate
for letra in texto:
    print(letra)
print()
"""
O resultado é exatemente o mesmo, mas por ser uma possibilidade finita, a iteração fica extremamente mais simples
e compreensivel
"""

texto = 'Python'
# Apesar de nao ter um contador, podemos colocar um com a função enumerate
for n, letra in enumerate(texto):  # Esta variavel n é o contado do enumrate, ela quem vai servir para eu printar
    print(n, letra)

"""
Usa-se comumente a built in range para
Range tem 3 arguemtos: start(0), stop, step(1)
No exemplo range(5, 10, 1) o start é o 5, o stop é o 10, e o step (pule tal em tal) é o 1
Note: O STOP nao entra na conta, no caso, ele para no numero anterior ao stop
"""

for n in range(20, 10):  # Esse codigo nao executa nada pois o start é maior que o stop
    print(n)
print()

for n in range(20, 10, -1):  # Caso eu queria fazer o inverso, preciso "Descer os degraus"
    print(n)
print()

for n in range(20, 10, -2):  # Muda-se os degraus e o codigo acompanha
    print(n)
print()

for n in range(0, 100, 8):  # Acho os multiplos de 8
    print(n)
print()

for n in range(100):
    if n % 8 == 0:
        print(n)
print()

texto = 'Python'
nova_str = ''

for letra in texto:
    if letra == 't':
        nova_str = nova_str + letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
    else:
        nova_str += letra
print(nova_str)
print()

"""
Posso usar o continue e o break durante estes laços tambem
"""

texto = 'Python'
nova_str = ''

for letra in texto:
    if letra == 't':
        continue  # Vai fzer o PC voltar pro for
        nova_str = nova_str + letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
        break  # Vai quebrar o codigo DEPOIS de maiuscular o H
    else:
        nova_str += letra
print(nova_str)