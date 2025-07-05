"""
A função len conta a quantidade de caracteres dentro de uma STR, é util para limitador ou detectar o minimo de caracteres
necessarios para fazer um cadastro, por exemplo
NAO FUNCIONA COM TIPOS NUMERICOS (INT e FLOAT)
"""
user = input('Digite seu usuario: ')  # Neste caso, na minha plataforma é tem um minimo/max de caracteres
qnt_caracteres = len(user)  # Tambem conta o spacebar

print(user, qnt_caracteres, type(qnt_caracteres))  # A função len retorna sempre um int
if qnt_caracteres >= 6 and qnt_caracteres <= 10:  # É bom simplificar esse tipo de expressao assim: 6 < qnt_caracteres < 18
    print('Usuario valido')
else:
    print('Usuario invalido')

str1 = input('Digite algo: ')
str2 = input('Digite algo dnv: ')
print(f'A quantidade de caracteres de str1 é {len(str1)} e a de str2 é {len(str2)} e a das duas juntas'
      f' é {len(str1) + len(str2)}')
"""
Em python tudo sao objetios
O len funciona apenas e somente com letras
"""




