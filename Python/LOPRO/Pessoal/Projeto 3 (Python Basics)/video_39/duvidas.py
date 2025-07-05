"""

"""
secret = 'Python'
secreto_temporario = ''
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
    digitadas.append(letra)
    print(digitadas)
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



