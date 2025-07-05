'''
Operadores logicos, sao exatamente iguais os operadores logicos de raciciocinio logico
and precisa de duas expressoes
or precisa de duas expressoes
not inversor booleano
in
not in
'''
a = 2
b = 2
c = 3
print(bool(a == b or b < c))
print(bool(a == b and b > c))
'''
if a > c:
    print(f'C é maior que A')
else:
    print(f'A é menor que C')
'''
if not a > c:
    print(f'C é maior que A')
else:
    print(f'A é menor que C')
d = ''
f = 0  # Tambem considaro falso em booleano
if not d:
    print(f'pls, preencha o valor de D')
if not f:
    print(f'pls, preencha o valor de f')
nome = 'Matheus'
if 'e' in nome:
    print(f'Existe a letra U no nome')

nome_2 = 'Nathalie'
if 's' in nome_2:
    print(f'Existe a letra S no nome')
else:
    print(f'Nao tem S no nome')

nome_3 = 'Carlos'
if 'C' not in nome_3:
    print(f'Nao tem C')
else:
    print(f'Tem sim')
