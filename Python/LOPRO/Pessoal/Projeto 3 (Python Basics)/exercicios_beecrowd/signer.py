criauser = input('Cadastro de usuario: ')
criasenha = input('Cadastro de senha: ')
criauserbd = criauser
criasenhabd = criasenha
loginuser = input('Usuario: ')
loginsenha = input('Senha: ')
stopper = 0
continuar = 'sim'
parar = 'não'
while loginuser != criauserbd or loginsenha != criasenhabd:
    print('Usuario nao cadastrado')
    stopper += 1
    loginuser = input('Usuario: ')
    loginsenha = input('Senha: ')
    if stopper == 3:
        exit(1)  # Ou break
if loginuser == criauserbd and loginsenha == criasenhabd:
    print('Login efetuado com sucesso!')
    while True:
        diauser = input('Qual o seu dia de aniversário (em numero): ')
        mesuser = input('Qual o seu mês de aniversário (em numero): ')
        if diauser.isnumeric() and mesuser.isnumeric():
            diauser = int(diauser)
            mesuser = int(mesuser)
            aquar = (21 <= diauser <= 31 or 1 <= diauser <= 18) and 1 <= mesuser <= 2
            peix = (19 <= diauser <= 28 or 1 <= diauser <= 20) and 2 <= mesuser <= 3
            ares = (21 <= diauser <= 31 or 1 <= diauser <= 20) and 3 <= mesuser <= 4
            touro = (21 <= diauser <= 30 or 1 <= diauser <= 20) and 4 <= mesuser <= 5
            gemio = (21 <= diauser <= 31 or 1 <= diauser <= 20) and 5 <= mesuser <= 6
            cancr = (21 <= diauser <= 30 or 1 <= diauser <= 22) and 6 <= mesuser <= 7
            leao = (23 <= diauser <= 31 or 1 <= diauser <= 22) and 7 <= mesuser <= 8
            virg = (23 <= diauser <= 30 or 1 <= diauser <= 22) and 8 <= mesuser <= 9
            libr = (23 <= diauser <= 31 or 1 <= diauser <= 22) and 9 <= mesuser <= 10
            escorp = (23 <= diauser <= 30 or 1 <= diauser <= 21) and 10 <= mesuser <= 11
            sarg = (22 <= diauser <= 31 or 1 <= diauser <= 21) and 11 <= mesuser <= 12
            capric = (22 <= diauser <= 31 or 1 <= diauser <= 20) and 12 <= mesuser <= 1
        else:
            usercontinue = input('Voce digitou um valor não numérico, deseja continuar? Y or N: ')
            if usercontinue == 'Y':
                continue
            elif usercontinue == 'N':
                print('Adeus')
                break

        if aquar:
            print('Você é de Aquario')
        elif peix:
            print('Você é de Peixes')
        elif ares:
            print('Você é de Ares')
        elif touro:
            print('Você é Meiralolkkkkkkkkkm, gado do krl')
        elif gemio:
            print('Você é de Gêmeos')
        elif cancr:
            print('Você é de Cancêr')
        elif leao:
            print('Você é de Leão')
        elif virg:
            print('Você é o Ledkkkkkkkk')
        elif libr:
            print('Você é de Libras')
        elif escorp:
            print('Você é de Escorpião')
        elif sarg:
            print('Você é de Sagitário')
        elif capric:
            print('Você é de Capricórnio')
        usercontinue2 = input('Deseja ver outro signo? Y or N: ')
        if usercontinue2 == 'Y':
            continue
        elif usercontinue2 == 'N':
            print('Adeus')
            break


'''
elif loginuser != criauserbd and loginsenha != criasenhabd:
    print('Usuario e Senha não cadastrados')
elif loginuser != criauserbd:
    print('Usuario não cadastrado!')
elif loginsenha != criasenhabd:
    print('Senha não cadastrada!')
'''
"""
Pedir mes dia do user > printar o signo > inputdeseja ver outro signo? > se sim, pede dnv mes e dia > senao mata o codigo "volte sempre"
COM WHILE
"""




