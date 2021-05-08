# Recebe o número de itens em uma lista e o valor de cada item e imprime o dobro do valor deles na ordem inversa
# Receives the number of items in a list and each item value, then prints their double in the reverse order

lista = []
n = int(input('Insira o número de itens da lista: '))

for cont in range (1, n + 1):

    lista.append(int(input('Insira o item: ')))

lista.reverse()

for i in lista:

    print(i * 2)