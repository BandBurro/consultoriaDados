"""
padaria > passa o produto um por um no scanner > cada uma das escaneadas da o valor de UM produto > quanto foi o
total da conta > para encerrar a execução do codigo vou passar o valor 0 > ao passar o valor 0, printa o valor TOTAL
"""

userstart = input('Deseja escanear produtos? Y ou N ')
print('Codigo de produtos:')
print('pao 1, pres 2, qeij 3')
print('lte 4, ovo 5, slgdo 6')
print()
pao = 1
paovalor = 2.5
pres = 2
presvalor = 1.6
qeij = 3
qeijvalor = 1.5
lte = 4
ltevalor = 3
ovo = 5
ovovalor = 4
slgdo = 6
slgdovalor = 5
acumulador = 0.0

while True:
    if userstart == 'Y':
        print()
        print('Total', acumulador)
        user = input('Digite o codigo dos seus produtos, cada uma vez que digita o codigo, será contada uma unidade: ')
        print()
        print('Caso queira encerrar a contagem, digite qualquer valor acima de 6')
        if user == '1':
            acumulador += paovalor
        elif user == '2':
            acumulador += presvalor
        elif user == '3':
            acumulador += qeijvalor
        elif user == '4':
            acumulador += ltevalor
        elif user == '5':
            acumulador += ovovalor
        elif user == '6':
            acumulador += slgdovalor
        print('Total', acumulador)
        while user <= '6':
            paovalor = float(paovalor)
            presvalor = float(presvalor)
            qeijvalor = float(qeijvalor)
            ltevalor = int(ltevalor)
            ovovalor = int(ovovalor)
            slgdovalor = int(slgdovalor)
            acumulador = float(acumulador)
            user = input('Digite o codigo dos seus produtos, cada uma vez que digita o codigo, será contada uma unidade: ')
            if user == '1':
                acumulador += paovalor
            elif user == '2':
                acumulador += presvalor
            elif user == '3':
                acumulador += qeijvalor
            elif user == '4':
                acumulador += ltevalor
            elif user == '5':
                acumulador += ovovalor
            elif user == '6':
                acumulador += slgdovalor
            print('Total: ', acumulador)
        else:
            print('Adeus')
            break
    elif userstart == 'N':
        print('Adeus')
        break















