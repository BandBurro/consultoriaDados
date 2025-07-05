'''
Primeiramente, dar-se-a um valor relacionado a função no jogo para cada objetivo conquistado ou adquirido
Esses objetivos terão valores maiores ou menores a depender da sua role
Caso esteja ADC, por exemplo, o numero de minions por minuto contará mais do que caso você esteja jogando JG
Entrada: Role, kills, assists, mortes, CS/MIN, baron e dragão
Saida: O valor unitario de cada um dos objetivos assim como o valor total, tudo isso a depender da role escolhida
Obs: Fazer primeiro
'''

role = input(f'Qual sua Role (ADC ou JG)? ').lower()
elo = input(f'Qual seu Elo atual? ')
tempo_jogo = input(f'Joga há quanto tempo (em anos)? ')
proxima_etapa = input(f'Preencha as perguntas abaixo com os dados da sua ultima partida (pressione enter):')
drag = int(input(f'Quantos dragões abatidos? '))
pontuação_drag_adc = drag * 1
pontuação_drag_jg = drag * 3
kills = int(input(f'Quantos abates? '))
pontuação_kills_adc = kills * 2
pontuação_kills_jg = kills * 2
assists = int(input(f'Quantas assistencias? '))
pontuação_assist_adc = assists * 1
pontuação_assist_jg = assists * 2
mortes = int(input(f'Quantas mortes? '))
pontuação_mortes_adc = mortes * 2
pontuação_mortes_jg = mortes * 2
csmin = int(input(f'Quantos minions por minuto? '))
pontuação_csmin_adc = csmin * 4
pontuação_csmin_jg = csmin * 2

total_adc = (pontuação_drag_adc+pontuação_kills_adc+pontuação_assist_adc+pontuação_csmin_adc)-pontuação_mortes_adc
total_jg = (pontuação_csmin_jg+pontuação_kills_jg+pontuação_assist_jg+pontuação_drag_jg)-pontuação_mortes_jg

if 'adc' in role:
    print('')
    print('Sua pontuação em Drags foi:', pontuação_drag_adc)
    print('Sua pontuação em Kills foi:', pontuação_kills_adc)
    print('Sua pontuação em Assists foi:', pontuação_assist_adc)
    print('Sua pontuação em Mortes foi:', - (pontuação_mortes_adc))
    print('Sua pontuação em CS/Min foi:', pontuação_csmin_adc)
    print('Sua pontuação Total é (Mortes contam negativamente):', total_adc)

if "jg" in role:
    print('')
    print('Sua pontuação em Drags foi:', pontuação_drag_jg)
    print('Sua pontuação em Kills foi:', pontuação_kills_jg)
    print('Sua pontuação em Assists foi:', pontuação_assist_jg)
    print('Sua pontuação em Mortes foi:', - (pontuação_mortes_jg))
    print('Sua pontuação em CS/Min foi:', pontuação_csmin_jg)
    print('Sua pontuação Total é (Mortes contam negativamente):', total_jg)
