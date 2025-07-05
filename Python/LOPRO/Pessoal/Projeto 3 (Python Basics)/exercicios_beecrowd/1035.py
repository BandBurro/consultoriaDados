# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D
# for maior que a soma de A e B e se C e D, ambos,
# forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

A = int(input('A = '))
B = int(input('B = '))
C = int(input('C = '))
D = int(input('D = '))
var_1 = B > C
var_2 = D > A
var_3 = (C + D) > (A + B)
var_4 = C and D > 0
var_5 = A % 2 == 0
if var_1 and var_2 and var_3 and var_4 and var_5:
    print('Valores Aceitos')
else:
    print('Valores não Aceitos')





# Não consigo fazer pois precisa de lista de numeros pares e impares



