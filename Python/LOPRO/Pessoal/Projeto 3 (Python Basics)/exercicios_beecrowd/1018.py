'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) em que o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.
'''

valor = int(input('Coloque um valor de 0 a 1.000.000R$: '))
if valor < 0 or valor > 1000000:
    print('Quantia inválida')
ced100 = int(valor)  //100
print('Cédulas de 100:', ced100)
restoced100 = int(valor) % 100
ced50 = restoced100 // 50
print('Cédulas de 50:', ced50)
restoced50 = int(restoced100) % 50
ced20 = restoced50 // 20
print('Cédulas de 20:', ced20)
restoced20 = int(restoced50) % 20
ced10 = restoced20 // 10
print('Cédulas de 10:', ced10)
restoced10 = int(restoced20) % 10
ced5 = restoced10 // 5
print('Cédulas de 5:', ced5)
restoced5 = int(restoced10) % 5
ced2 = restoced5 // 2
print('Cédulas de 2:', ced2)
restoced2 = int(restoced5) % 2
ced1 = restoced2 // 1
print('Cédulas de 1:', ced1)



