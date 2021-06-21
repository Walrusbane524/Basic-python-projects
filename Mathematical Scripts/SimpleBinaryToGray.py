#Recebe um número binário do usuário, converte e imprime o mesmo valor em Gray.
#Receives a binary number from the user, converts and prints the same value in Gray.

#Recebe o número binário como imput, divide em dígitos e define algumas variáveis.
#Receives the bunary number as input, splits it into digits and defines some variables.
number = input("Insira o número binário que deseja converter em Gray: ")
binary = list(number)
grayDigits = {}
gray = ''
i = 0
n = ''

while i < len(binary) :

    #Repete o dígito mais significativo.
    #Repeats the most significant digit.
    if i == 0:

        grayDigits[0] = binary[0]

    #Verifica se o dígito binário atual é igual ao anterior e, se for, adiciona '0' ao próximo dígito do número gray.
    #Checks if the current binary digit is equal to the previous and, if so, adds '0' as the next digit to the gray number.
    elif i != 0 and binary[i] == binary[i - 1]:

        grayDigits[i] = '0'
    
    #Verifica se o dígito binário atual é diferente do anterior e, se for, adiciona '1' ao próximo dígito do número gray.
    #Checks if the current binary digit is different from the previous and, if so, adds '1' as the next digit to the gray number.
    elif i != 0 and binary[i] != binary[i - 1]:

        grayDigits[i] = '1'
    
    i += 1

#Une os dígitos do número em gray.
#Unites the gray number digits.
for x in grayDigits:

    gray += grayDigits[x]

#Imprime o resultado.
#Prints the result.
print("O número convertido em gray é:", gray)