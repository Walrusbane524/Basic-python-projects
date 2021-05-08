# Recebe o número de elefantes do usuário e imprime a música com o número correto de repetições da palavra incomodam
# Receives the number of elefants from the user and prints the music with the correct number of 'incomodam' repetitions
# (This program was made around a brazilian kids song, so this might make no sense in english)

n = int(input('Insira o número de elefantes: '))
print('\n\n')

for cont in range (1, (n + 1)):

    #Se o número de elefantes for 1.
    #If the number of elefants is equal to 1.
    if cont == 1:
        
        print(cont ,'elefante incomoda muita gente.')
    
    #Se for um número ímpar de elefantes e não é o primeiro elefante.
    #If the number of elefants is an odd number and different from 1.
    elif (cont % 2) != 0 and cont != 1:
        
        print(cont, 'elefantes incomodam muita gente.')
    
    #Caso seja um número par de elefantes.
    #If the number of elefants is an even number.
    else:
        
        inco = 'incomodam '
        
        #Soma 'incomodam ' á variável inco de acordo com o número de elefantes.
        #Adds 'incomodam' to the inco variable according to the number of elefants.
        for cont2 in range (1, cont):
            inco += 'incomodam '
        
        print(cont , 'elefantes ' + inco + 'muito mais.')