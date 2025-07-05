cpf = '16899535009'
novo_cpf = cpf[:-2]
for index in range(19):  # Do 0 ao 18 da 19 voltas
    if index > 8:
        index -= 9  # Com ete codigo meu loop vai voltar ao 0 apos concluir o primeiro loop, vai de 0 a 8 dps de 0 a 9, totalizando as 19 voltas que eu preciso
    print(cpf[index])
