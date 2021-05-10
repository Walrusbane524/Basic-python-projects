## Recebe os elementos de uma matrix 2x2, calcula e imprime a sua determinante.
# Receives the 2x2 matrix elements, calculates and prints its determinant.

lista = []
l = 2
c = 2

for i in range(0, c):
    listaTemp = []

    for i in range (0, l):
    
        listaTemp.append(int(input('Insira o item: ')))
    
    lista.append(listaTemp)

determinante = (lista[0][0] * lista[1][1]) - (lista[0][1] * lista[1][0])

print('A determinante é:', determinante)