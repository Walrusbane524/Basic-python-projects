## Recebe uma lista de números do usuário e verifica se essa lista representa uma progressão aritmética, imprimindo a razão se for.
# Receives a list of numbers from the user and checks if that list represents an arithmetic progression, printing the ratio if it is.

## Recebe todos os itens da lista, separados por ', ' e os organiza em uma lista temporária de strings.
# Receives all of the list's items, separated by ', ' and arranges them in a temporary list of strings
itens = input('Insira todos os números da lista, separados por vírgula e espaço (", "):\n\n')
listaTemp = itens.split(', ')
lista = []
count = 0
pa = True

## Transforma cada item da lista temporária em um float e insere na lista verdadeira.
# Transforms each item from the temporary list into a float and inserts in the real list.
for i in listaTemp:

    lista.append(float(i))

## Calcula a razão da progressão.
# Calculates the progression's ratio.
razao = lista[1] - lista[0]

## Roda enquanto count é menor ou igual ao penúltimo índice da lista.
# Runs while count is smaller or equal to the second last index of the list.
while count <= (len(lista) - 2) and pa == True:
    
    ## Roda até verificar o penúltimo item ou enquanto os items seguirem a progressão.
    # Runs until it checks the second last item or as long as the items follow the progression.
    if count < len(lista) - 2 and (lista[count] + razao) == lista[(count + 1)]:
    
        count += 1
    
    ## Roda quando ele verifica o último item com sucesso.
    # Runs when it checks the last item sucessfuly.
    elif count == len(lista) - 2 and (lista[count] + razao) == lista[(count + 1)]:

        print ('É PA e a razão é', razao)
        break

    ## Roda quando o item de index count + razão não é igual ao próximo item da lista.
    # Runs when the item of index count + ratio is not equal to the next item on the list.
    else:

        pa = False
        print('Não é PA.')