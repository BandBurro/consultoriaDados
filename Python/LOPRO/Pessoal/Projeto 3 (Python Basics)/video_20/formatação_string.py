'''
as vezes, um print pode parecer muito complexo, como o "print(nome, 'tem', idade, 'de idade e seu IMC é', imc)" que tem muitas
virgulas, aspas e tals, portanto, as vezes podemos usar "f strings", que é basicamente por um "f" logo antes da string
como no exemplo: print(f'gfdiujhasdiojuih'), em paralelo ao print anterior, farei um f string com o mesmo formato
print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc})
'''

nome = "gfonhdopksadfhiujgds"  # Str
idade = 25  # Int
altura = 2.84  # Float
maioridade = 18 < idade  # Bool
peso = 80
data_1 = True  # Bool (neste caso é um valor booleano explícito, ja digido o valor em True ou False direto, começando com maisculo)
data_atual = 2019  # Int
imc = peso / (altura ** 2)


'''
Alem de nao precisar me preocupar com os detalhes de algo ser string ou não, posso por um dois pontos e o numero de casas decimais
que eu quero que sejam exibidas em um float muito extenso, como no caso do IMC, com o comando ":.nf"
'''
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc}')
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
'''
Tambem posso usar o comando .format para poder facilitar minha print da seguinte forma
'''
print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc))
'''
Para poder pegar apenas as casas decimais de algum float com o .format, eu posso botar dentro dos {} correspondentes o
comando de dois pontos
'''
print('{} tem {} anos de idade e seu IMC é {:.3f}'.format(nome, idade, imc))
'''
O comando de .format enumera as coisas entre parenteses de 0 ate n, começando a primeira variavel no 0 ate o infinito
,portanto, posso substituir os valores pelos seus correspondentes numericos, como no exemplo
'''
print('{0} tem {1} anos de idade e seu IMC é {2}'.format(nome, idade, imc))
'''
Inclusive, justamente por ser organizado numericamente de 0 ate o numero final, posso reorganizar com os numeros do jeito
que eu bem quiser
'''
print('{0} {2} {1} {0}{2} tem {1} anos de idade e seu IMC é {2}'.format(nome, idade, imc))  # Os espaços entre os {}
# é contado
#  normalmente como se fosse uma string, note, ao executar, que os 3 primeiros numeros tem espaço, os outros 2 não
'''
Tambem é possivel trocar os numerais padroes por qualquer outra variavel que eu quiser, como por exemplo
'''
print('{n} tem {i} anos de idade e seu IMC é {m}'.format(n=nome, i=idade, m=imc))

