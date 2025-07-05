"""
Validando um CPF
CPF = 168,995,350-09                                 1 * 11 = 11        <<<<
1 * 10 = 10                                          6 * 10 = 60
6 * 9 = 54                                           8 * 9 = 72
8 * 8 = 64                                           9 * 8 = 72
9 * 7 = 63                                           9 * 7 = 63
9 * 6 = 54                                           5 * 6 = 30
5 * 5 = 25                                           3 * 5 = 15
3 * 4 = 12                                           5 * 4 = 20
5 * 3 = 15                                           0 * 3 = 0
0 * 2 = 0                                    >>>>    0 * 2 = 0

   297                                                  343
11 - (297 % 11) = 11                            11 - (343 % 11) = 9
11 > 9 = 0
Digito 1 = 0                                    Digito 2 = 9
"""
"""
cpf = input('Digite um CPF ')
# novocpf = input()
digito1 = int(cpf[0])
digito2 = int(cpf[1])
digito3 = int(cpf[2])
digito4 = int(cpf[3])
digito5 = int(cpf[4])
digito6 = int(cpf[5])
digito7 = int(cpf[6])
digito8 = int(cpf[7])
digito9 = int(cpf[8])
digito10 = int(cpf[9])
digito11 = int(cpf[10])

var1 = digito1 * 10
var2 = digito2 * 9
var3 = digito3 * 8
var4 = digito4 * 7
var5 = digito5 * 6
var6 = digito6 * 5
var7 = digito7 * 4
var8 = digito8 * 3
var9 = digito9 * 2
totalvars = var1+var2+var3+var4+var5+var6+var7+var8+var9
verificprimeirodigito = 11 - totalvars % 11
if verificprimeirodigito >= 9:
    primeirodigito = 0
    print(primeirodigito)

var1_1 = digito1 * 11
var2_1 = digito2 * 10
var3_1 = digito3 * 9
var4_1 = digito4 * 8
var5_1 = digito5 * 7
var6_1 = digito6 * 6
var7_1 = digito7 * 5
var8_1 = digito8 * 4
var9_1 = digito9 * 3
var10_1 = primeirodigito * 2
totalvars_ = var1_1+var2_1+var3_1+var4_1+var5_1+var6_1+var7_1+var8_1+var9_1+var10_1
segundodigito = 11 - totalvars_ % 11
print(segundodigito)

if primeirodigito == digito10 and segundodigito == digito11:
    print('CPF Valido')
else:
    print('CPF Invalido')
"""

cpf = '16899535009'  # Basta mudar o cpf dentre aspas para verifica-lo
novo_cpf = cpf[:-2]  # Ou posso fazer cpf[:9], lembrando que todo valor iteravel tem um valor indo e voltando ( com o - fica voltando)
"""
Preciso loopear 19 vezes para fazer todas as multiplicações, 9 na esquerda e 10 na direita, a da direita tem uma a mais
pois tem o valor do digito1 adicionado na sua conta
"""
reverso = 10  # Variavel usada pra começar o valor das multiplicações, a primeira "coluna" de multiplicações começa no 10, assim que ela chegar no 2, vai virar um '11' para poder
total = 0  # Variavel "vazia" que vai acumular os valores de soma, pra dps fazer total % 11 pro primeiro e segundo digito
for index in range(19):  # Do 0 ao 18 da 19 voltas
    if index > 8:
        index -= 9  # Com ete codigo meu loop vai voltar ao 0 apos concluir o primeiro loop, vai de 0 a 8 dps de 0 a 9, totalizando as 19 voltas que eu preciso
    #print(cpf[index], index, reverso)
    total += int(novo_cpf[index]) * reverso
    reverso -= 1  # Esta subtração é o dropdown ate o 2, para depois voltar ao 11 no codigo da linha 84, e descer ate o 2 novamente
    if reverso < 2:  # Pq todas as multiplicações param em 2
        reverso = 11  # Que é a primeira multiplicação da segunda coluna
        d = 11 - (total % 11)  # Variavel que vai guardar o valor do primeiro digito

        if d > 9:  # Verificação do primeiro digito
            d = 0  # O valor do primeiro digito
        total = 0  # Reseta a variavel "total += int(novo_cpf[index]) * reverso"
        novo_cpf += str(d)  # Transformo em STR pois quero colocalo no valor final em texto, que é quase por total uma STR

#print(novo_cpf)  # se nao fosse o "novo_cpf += str(d)" teria um print de tudo menos os dois ultimos digitos, entao tudo menos o 09 final
if cpf == novo_cpf:
    print('Valido')
else:
    print('Invalido')
