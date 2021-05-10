## Recebe uma frase de um usuário, identifica a palavra mais frequente, imprime ela e as vezes que ela foi repetida.
# Receives a phrase from the user, identifies the most frequently used word, prints it and how many times it was repeated.

c = 0
lista = []

frase = input('Insira uma frase: ')
listaTemp = frase.split(',')

for i in range (0, (len(listaTemp))):

    lista.extend(listaTemp[i].split(' '))

lista.sort()

while c <= len(lista) - 1:
    
    if (lista.count(lista[c])) > rep:

        rep = lista.count(lista[c])
        itemIndex = c
    
    c += 1


print('A palavra mais frequente é', lista[itemIndex], 'e foi repetida', rep, 'vezes.')