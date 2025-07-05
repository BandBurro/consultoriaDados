# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
# Utilize a fórmula: MaiorAB = (a+b+abs(a-b))/2

int1 = int(input())
int2 = int(input())
int3 = int(input())
int1EhMaior = (int1 > int2) and (int1 > int3)
int2EhMaior = (int2 > int1) and (int2 > int3)
int3EhMaior = (int3 > int2) and (int3 > int1)
if int1EhMaior:
    print(int1, 'é o maior valor')
elif int2EhMaior:
    print(int2, 'é o maior valor')
elif int3EhMaior:
    print(f'{int3} é o maior valor')

