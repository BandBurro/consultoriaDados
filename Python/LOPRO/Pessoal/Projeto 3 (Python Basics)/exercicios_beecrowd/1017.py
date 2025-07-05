# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel
# que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa.
# Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h).
# Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários.
# Mostre o valor com 3 casas decimais após o ponto.

tempo = int(input('Tempo gasto na viagem em horas = '))
vel_med = int(input('Velocidade média em KM/H = '))
distancia = vel_med * tempo
gasolina = 12
gasolina_neces = distancia / gasolina
print(f'Gasolina Necessaria é: {gasolina_neces:.3f}L')

'''
tempo_gasto1 = 10
velocidade1 = 85
distancia1 = velocidade1 * tempo_gasto1
litro = 12
gas1 = distancia1 / litro
'''
