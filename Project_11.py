# Recebe a lista inteira do usuário de uma vez, com cada item separado por ', ' e imprime a soma
# De todos os itens, o maior e menor número e a média aritmética

# Receives the entire list from the user, with each item separated with ', ' and prints the sum 
# of all items, the smallest and biggest number, and the arithmetic average

itens = input('Insira todos os números da lista, separados por vírgula e espaço (", "):\n\n')
listaTemp = itens.split(', ')
lista = []

for i in listaTemp:

    lista.append(float(i))

print('A soma dos números da lista é:', sum(lista))
print('O menor número da lista é:', min(lista))
print('O maior número da lista é:', max(lista))
print('A média aritmética dos ítens da lista é:', ( (sum(lista) ) / (len(lista) ) ) )