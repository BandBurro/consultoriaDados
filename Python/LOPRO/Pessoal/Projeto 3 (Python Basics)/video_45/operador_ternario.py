"""
Operador ternario
"""
logged_user = True  # troco o valor de True ou False a depender do estado do usuario, se estiver logado ou nao
if logged_user:
    msg = 'User logado'
else:
    msg = 'Usuario precisa logar'
print(msg)
print()
"""

"""
print('Operador Ternario')
print()
logged_user = True
msg = 'User logado' if logged_user else 'Usuario precisa logar'
print(msg)
"""

"""
print()
idade = 18
if idade >= 18:
    print('Pode Acessar')
else:
    print('Nao pode Acessar')
print()
print('Operador Ternario')
print()
idade = 18  # Posso colocar a idade como um input idade = input()
demaior = (idade >= 18)
msg = 'Pode acessar' if demaior else 'Nao pode acessar'
print(msg)
"""
Posso colocar a idade como um input idade = input()
"""
print()
print('Operador Ternario')
print()
idade = input('Idade ')
if not idade.isnumeric():
    print('Digite um numero')
else:
    idade = int(idade)
    demaior = (idade >= 18)
    msg = 'Pode acessar' if demaior else 'Nao pode acessar'
    print(msg)



