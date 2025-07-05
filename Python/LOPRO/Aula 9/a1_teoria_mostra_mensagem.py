"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Implemente uma função pra mostrar a mensagem fixa "Exemplo de
mensagem fixa em def". Ela não recebe nada e não retorna nada.
  Crie o programa principal (função main) para chamar a funçao.

"""

# O def indica o início de uma função (uma rotina)
def mostra_mensagem():                  # Assinatura da função
    print("Exemplo de mensagem fixa em def.")

# A função (def) mostra_mensagem é chamada dentro do main
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':          # Atalho: mai + tecla<tab>
    mostra_mensagem()               # Chama a função sem passar nada
''' --- ALTERAÇÕES:
a. Na função principal, mostre uma mensagem antes de chamar a função 
b. Na função principal, mostre uma mensagem depois de chamar a função
c. Crie a função mostra_mensagem_2, ela recebe uma frase e mostra a
   frase recebida. Na função principal, chame a função passando uma 
   mensagem
d. No main, chame a função mostra_mensagem2 mais uma vez, passe a 
   mensagem
e. No main, use o input para ler uma mensagem e chame a função 
   mostra_mensagem2 mais uma vez passando a mensagem lida.
    ----- DICAS:
if __name__ == '__main__':  # Atalho: mai + tecla<tab>
    print("Mensagem antes de chamar a função")  # No início do main     # a.
    mostra_mensagem()                  # Chama a função sem passar nada
    print("Mensagem depois de chamar a função")                         # b.
def mostra_mensagem_2(variavel_1):                                      # c.
    print(variavel_1)
    ...                     # No final do main                      
    mostra_mensagem_2("Mensagem 1 passada pra função")  # Solução 1  
    var = "Mensagem 2 passada pra função"               # Solução 2     # d.
    mostra_mensagem_2(var)             
    var = input("Digite uma mensagem")                  # Solução 3     # e.
    mostra_mensagem_2(var)

'''
