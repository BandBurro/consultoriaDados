criauser = input('Cadastro de usuario: ')
criasenha = input('Cadastro de senha: ')
criauserbd = criauser
criasenhabd = criasenha
userdb = []
acumuladora = 0

while criauser == userdb:
    print('Usuário ja cadastrado')
    acumuladora += 1
    criauser = input('Cadastro de usuario: ')
    criasenha = input('Cadastro de senha: ')
    userdb.append(criauser)
    if acumuladora == 3:
        print('Muitas tentativas, vc é bot?')
        break
else:
    loginuser = input('Usuario: ')
    loginsenha = input('Senha: ')
    if loginuser == criauserbd and loginsenha == criasenhabd:
        print('Login efetuado com sucesso!')
    elif loginuser != criauserbd and loginsenha != criasenhabd:
        print('Usuario e Senha não cadastrados')
    elif loginuser != criauserbd:
        print('Usuario não cadastrado!')
    elif loginsenha != criasenhabd:
        print('Senha não cadastrada!')

'''
errar senha ou user > pede dnv ate o limite de 3 > muitas tentativas, vc é raid bot?
COM WHILE
# Feito
'''
'''
fazer o mesmo exercicio trocando o hardcode de 'matias' por lista, linha 7
ao tentar criar um usuario ja existente, printar a lista de usuarios ja cadastrados
'''




