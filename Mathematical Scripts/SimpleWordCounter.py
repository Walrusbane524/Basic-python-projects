## Recebe uma frase de um usuário, identifica a palavra mais frequente, imprime ela e as vezes que ela foi usada.
# Receives a phrase from the user, identifies the most frequently used word, prints it and how many times it was used.

c = 0
itemIndex = 0
rep = 0
lista = []

## Recebe a frase do usuário e a divide nas vírgulas.
# Receives the phrase from the user and divides it on commas.
frase = input('Insira uma frase: ')
listaTemp = frase.split(',')

## Divide a list nos espaços.
# Divides the remaining sections of the phrase into words.
for i in range (0, (len(listaTemp))):

    lista.extend(listaTemp[i].split(' '))

## Organiza as palavras da lista em ordem alfabética.
# Organizes the words from the list in alphabetical order.
lista.sort()

## Pega o índice da palavra mais usada e a quantidade de vezes que ela foi usada.
# Acquires the index of the most used word and how many times it was used.
while c <= len(lista) - 1:
    
    if (lista.count(lista[c])) > rep:

        rep = (lista.count(lista[c]))
        itemIndex = c
    
    c += 1

## Imprime o resultado.
# Prints the result.
print('A palavra mais frequente é', lista[itemIndex], 'e foi usada', rep, 'vezes.')