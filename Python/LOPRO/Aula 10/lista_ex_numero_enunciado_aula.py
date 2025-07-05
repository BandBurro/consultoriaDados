"""            Comentários de várias linhas     -     Prof. Barbosa
Dicas: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Implemente um programa com os conceitos de lista (array - vetor) e resolva
todos estes problemas num único programa .py.

- Na sala on-line, veja a sintaxe de lista no arquivo "Teoria lista.docx"

a- Crie uma lista vazia.
b- Leia vários números digitados pelo usuário e os armazene na lista. Use repetição.
c- Mostre a lista na horizontal;
d- Mostre a lista na vertical;
e- Mostre a quantidade de elementos armazenados na lista, não use contador;
f- Mostre a soma dos valores da lista, não use somador;
g- Mostre o maior valor da lista;
h- Mostre o menor valor da lista;
i- Faça uma pesquisa. Leia um valor digitado pelo usuário e verificar se ele está na lista;
j- No item anterior, mostre também a posição (índice) do valor encontrado;
k- Mostre a lista na ordem crescente;
l- Insira (acrescente) o valor 33 na posição (índice) 1 da lista;
m- Mostre a lista na ordem decrescente;
n- Calcule e mostre a média aritmética dos valores da lista;
o- Mostre a média com três casas decimais;
p- Mostre a quantidade de valores maior que dez na lista.
q- Porcentagem dos números maiores que dez da lista.
r- Rmova o valor 33 da lista e depois mostre a lista.            """
lista = []       # Cria uma lista vazia                             # a.
print('Digite [0] pra sair')                                        # b.
while True:
    valor = int(input("Valor: "))
    if valor == 0:          # Se condição de saída
        break               # Sai de uma estrutura de repetição
    lista.append(valor)     # Acrescenta o valor no final da lista
print("Valores da lista na horizontal:\n", lista)                   # c.
print("Valores da lista na vertical:")                              # d
for numero in lista:
    print(numero)
print('Quantidade de elementos da lista:', len(lista))              # e.
print('Soma dos elementos da lista:', sum(lista))                   # f.
print('Maior valor:', max(lista))                                   # g.
print('Menor valor:', min(lista))                                   # h.
pesquisa = int(input("Valor da pesquisa: "))                        # i.
if pesquisa in lista:
    print("Valor encontrado.")
    posicao = lista.index(pesquisa)          # Solução 1            # j.
    print('Posição da pesquisa:', posicao)
else:
    print("Valor não encontrado.")
print('Antes do sort():\n', lista)                                  # k.
lista.sort()  # lista.sort(reverse=False)   # Solução 1
print('Depois do sort():\n', lista)
lista.insert(1, 33) # lista.insert(indice, item)     # l.
print(lista)
# lista.reverse()   # Errado, não coloca na ordem decrescente       # m.
# print(lista)
lista.sort()                                # Solução 1
lista.reverse()
print('Ordem decrescente:\n', lista)
