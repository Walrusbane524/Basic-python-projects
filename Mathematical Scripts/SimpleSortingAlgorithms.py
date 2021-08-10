# Cria e ordena uma lista com 100 mil inteiros aleatórios usando bubble-sort e selection-sort.
## Creates and sorts a list with 100 thousand random integers using bubble-sort and selection-sort.

# Usados para preencher a lista com números aleatórios e medir o tempo de execução dos algoritmos.
## Used to fill the lists with random integers and measure the exectution time of the algorithms.
import random
import time

# Função do algoritmo selection-sort.
## Selection-sort algorithm function
def selectionSort(v):

    # Marca o tempo inicial.
    ## Marks the initial time.
    ini = time.time()
    
    # Cria as variáveis usadas no algoritmo.
    ## Creates the variables used in the algorithm.
    maior = 0
    menor = 0

    # Executa o selection-sort.
    ## Runs selection-sort.
    for x in range (0, len(v) - 1):

        maior = v[x]

        for y in range (x + 1, len(v)):

            menor = v[y]
    
            if maior > menor:
                v[y] = maior
                v[x] = menor

                
                maior = menor

    # Marca o tempo final e calcula o tempo em minutos e segundos.
    ## Marks the finishing time and calculates the execution time in minutes and seconds.
    fim = time.time()
    tempo = fim - ini
    minutos = tempo//60
    segundos = tempo % 60

    # Imprime o tempo de execução do algoritmo.
    ## Prints the execution time of the algorithm.
    print("Selection-sort: %d minutos e %d segundos" % (minutos, segundos))
    return v

# Função do algoritmo bubble-sort.
## Bubble-sort algorithm function.
def bubbleSort(v):

    # Marca o tempo inicial.
    ## Marks the start time.
    ini = time.time()

    # Cria as variáveis usadas no algoritmo.
    ## Creates the variables used in the algorithm.
    maior = 0
    menor = 0
    ordenado = False

    # Executa o bubble-sort.
    ## Runs bubble-sort.
    while ordenado != True:

        ordenado = True

        for x in range(0, len(v) - 1):

            maior = v[x]
            menor = v[x + 1]

            if maior > menor:

                ordenado = False
                v[x + 1] = maior
                v[x] = menor

    # Marca o tempo final e calcula o tempo em minutos e segundos.
    ## Marks the finishing time and calculates the execution time in minutes and seconds.
    fim = time.time()
    tempo = fim - ini
    minutos = tempo//60
    segundos = tempo % 60

    # Imprime o tempo de execução do algoritmo.
    ## Prints the execution time of the algorithm.
    print("Bubble-sort: %d minutos e %d segundos" % (minutos, segundos))
    return v

# Cria as listas usadas
v1 = []
v2 = []

# Preenche as listas com 100 mil números inteiros aleatórios entre 1 e 1 milhão.
## Fills the lists with 100 thousand random integers ranging from 1 and 1 million.
for i in range(0, 100000):
    v1.append(random.randint(1, 1000000))
    v2.append(random.randint(1, 1000000))

# Executa as funções.
## Runs the funcions.
v1 = selectionSort(v1)
v2 = bubbleSort(v2)