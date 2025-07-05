userdb = []
senhadb = []
acumuladora = 0
# cadastros = [['asd', 'asd'], ['zxc', 'zxc']]
cadastros = []
while True:
    cmd = input('Deseja Logar ou Criar uma Conta? Digite 1 para Logar e 2 para Criar ')
    if cmd == '1':
        cadastroencontrado = False
        loginuser = input('Usuario: ')
        loginsenha = input('Senha: ')
        for i in cadastros:
            if loginuser == i[0] and loginsenha in i[1]:
                print('Login efetuado com sucesso!')
                cadastroencontrado = True
        if not cadastroencontrado:
            print('Email ou Senha não cadastrado')
    if cmd == '2':
        criauser = input('Cadastro de usuario: ')
        criasenha = input('Cadastro de senha: ')
        if criauser in userdb:
            print('Usuário ja cadastrado')
            print(f'Estes são os usarios ja cadastros: {userdb}')
            acumuladora += 1
        if acumuladora == 3:
            print('Muitas tentativas, vc é bot?')
            break
        if criauser in userdb:
            continue
        cadastro = []
        cadastro.append(criauser)
        cadastro.append(criasenha)
        cadastros.append(cadastro)






