tempuser = int(input('Informe o tempo total em Segundos: '))
temph = tempuser // 3600
print(temph, end=':')
temph_resto = tempuser % 3600
tempm = temph_resto // 60
print(tempm, end=':')
tempm_resto = tempuser % 60
print(tempm_resto)
