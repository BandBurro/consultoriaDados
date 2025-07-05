usuario = input(f'Nome de User: ')
senha = input(f'Senha do User: ')
usuario_bd = 'asd'
senha_bd = '123'
if usuario_bd == usuario and senha_bd == senha:
    print(f'Login efetuado com sucesso')
elif usuario_bd != usuario and senha_bd != senha:
    print(f'Senha e usuario incorretos')
elif senha_bd != senha:
    print(f'Senha Incorreta')
elif usuario_bd != usuario:
    print(f'Usuario Incorreto')


