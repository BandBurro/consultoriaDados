avo1 = 'Carlos'
avo2 = 'Maria'
filho1 = 'Marcos'
filho2 = 'Xenia'
filho3 = 'Eduarda'
conjugue1 = 'Marcela'
conjugue2 = 'Tarcio'
neto1_1 = 'Matias'
neto1_2 = 'Mathias'
neto2_1 = 'Martias'
neto2_2 = 'Maitias'
casal1 = filho1 + conjugue1
casal2 = filho2 + conjugue2
eduarda = False
print(f'{avo1} {avo2}')
print('{f1}+{c1} {f2}+{c2} {f3}'.format(f1=filho1, c1=conjugue1, f2=filho2, c2=conjugue2, f3=filho3))
print('{} e {} são filhos de {}, {} e {} são filhos de {}'.format(neto1_1, neto1_2, casal1, neto2_1, neto2_2, casal2))
print('Eduarda =', bool(eduarda))
