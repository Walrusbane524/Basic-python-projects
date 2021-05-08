# Recebe um número do usuário e verifica se ele é primo e mostrando o menor divisor dele caso não seja.
# Receives a number from the user and checks if it is a prime number and printing it's smaler divider in case it isn't;

import math

n = int(input('Insira o número que você deseja verificar: '))
cont = 1
calculando = True

n = (math.fabs(n))

if n != 1 and n != 0:

    while cont < (n//2) + 1 and calculando == True:
    
        cont += 1
        result = n % cont
    
        if result == 0:
        
            print('O número é divisível por', cont)
            calculando = False
    
        elif cont == (n//2) and result != 0:
        
            print('O número é primo')
            calculando = False

elif n != 0:
    
    print('O número é primo')

else:
    
    print ('O número é nulo')