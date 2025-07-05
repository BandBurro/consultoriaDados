codigo, qtt = input('Quantidade de Produtos: ').split()
cq = 4
cq_c = 1
xs = 4.50
xs_c = 2
xb = 5
xb_c = 3
trrd = 2
trrd_c = 4
rfgt = 1.50
rfgt_c = 5
if codigo == '1':
    cqt = cq * int(qtt)
    print(f'Total: {cqt} R$')

else:
    print('Codigo nao registrado')

if qtt == '3':
    cqt = cq * int(qtt)
    print(f'Total: {cqt} R$')

#else:
    #print('Codigo nao registrado')