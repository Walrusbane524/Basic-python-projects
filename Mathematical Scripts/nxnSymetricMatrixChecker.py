## Recebe o tamanho e os itens de uma matrix quadrada do usuário e verifica se a matriz é simétrica.
# Receives the size and items of a square matrix from the user and checks the matrix is symetric.

simetrico = True
lista = []
n = int(input('Insira o número de linhas e colunas da matriz: '))

## Impede o usuário de dar matrizes de 1 item, nulas ou de tamanho negativo.
# Stops the user from giving 1 item, null or negative sized matrixes.
if n > 1:

    ## Recebe cada item da matriz do usuário.
    # Receives each of the matrix items from the user.
    for i in range(0, n):
        listaTemp = []

        for i in range (0, n):
    
            listaTemp.append(int(input('Insira o item: ')))
    
        lista.append(listaTemp)

    ## Verifica se a matriz é simétrica.
    # Checks if the matrix is symetric.
    for l in range(0, n):

        if simetrico == True:

            for c in range(0, n):

                if (lista[l][c]) == (lista[c][l]):
                
                    simetrico = True

                else:

                    simetrico = False
    
    ## Imprime o resultado.
    # Prints the result.
    if simetrico == True:

        print('A matriz é simétrica')
    
    else:

        print('A matriz não é simétrica')

else:

    print('A matriz é inválida')

