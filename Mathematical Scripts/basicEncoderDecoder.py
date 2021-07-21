##Codifica strings ao transformá-las em binário, de binário para gray e de gray de volta para string.
#Encodes strings by transforming them into binary, from binary to gray and from gray into string again.

print('Bem-vindo ao Codificador.') #'Welcome to the encoder.'
print('O codificador usa os caracteres dentro da lista encodedChar,') #'The encoder uses characters from the list encodedChar'
print('tanto na codificação quanto na decodificação da string, e') #'when reading input as well as when encoding the string'
print('pode ser customizada dentro do código.\n') #'and can be customized inside the code.'

##Lista de caracteres. Adicione ou remova caracteres de acordo com os que você quer usar.
#List of characters. Add or remove characters to suit your needs.
encodedChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

def encoder():
    ##Define as variáveis usadas
    #Defines the variables used.
    string = input('Insira a sequência de caracteres que deseja codificar: ')
    inputChar = list(string)
    inputChar.reverse()
    value = 0
    binary = []
    gray = []
    codList = []
    cod = ''

    ##Converte o valor do index dos caracteres do input em valor decimal.
    #Converts the index value of the input characters into decimal.
    for x in encodedChar:
        index = 0
        while index < len(inputChar):
            if inputChar[index] == x:

                value += (encodedChar.index(x)) * ((len(encodedChar))**(index))

            index += 1

    ##Converte o valor em decimal para um em binário.
    #Converts the decimal value to binary.
    divRes = 1
    divRem = 1

    while divRes != 0:


        divRes = value // 2
        divRem = value % 2
        value = divRes

        binary.append(str(divRem))

    binary.reverse()

    ##Converte o valor em binário para gray.
    #Converts the binery value to gray.
    for i in range(0, (len(binary))):
    
        if i == 0:
            gray.append(binary[0])

        elif binary[i] != binary[i - 1]:
            gray.append('1')

        else:
            gray.append('0')
    
    gray.reverse()

    ##Converte o valor em gray para decimal.
    #Converts the gray value to decimal
    value = 0
    for i in range (0, len(gray)):
        value += int(gray[i]) * (2**(i))


    ##Converte o valor decimal para caractere usando seus valores de index.
    #Converts the decimal value to characters using their index values.
    divRes = 1
    divRem = 1

    while divRes != 0:

        divRes = value // (len(encodedChar))
        divRem = value % (len(encodedChar))
        value = divRes

        codList.append(encodedChar[divRem])

    codList.reverse()

    ##Une os caracteres codificados em uma string.
    #Unites the codified characters into a string.
    for i in codList:
        cod += i

    ##Mostra a string codificada.
    #Prints the encoded string.
    print('\nA sequência de caracteres codificadas é: ' + cod)

    ##Pergunta se o usuário quer codificar outra string.
    #Asks if the user wants to encode another string.
    again = input('\nInsira 1 se você gostaria de codificar ou decodificar outra sequência de caracteres: ')
    
    if again == '1':
        choice()

def decoder():

    ##Define as variáveis usadas
    #Defines the variables used.
    string = input('Insira a sequência de caracteres que deseja decodificar: ')
    inputChar = list(string)
    inputChar.reverse()
    value = 0
    binary = []
    gray = []
    codList = []
    cod = ''

    ##Converte o valor do index dos caracteres do input em valor decimal.
    #Converts the index value of the input characters into decimal.
    for x in encodedChar:
        index = 0
        while index < len(inputChar):
            if inputChar[index] == x:

                value += (encodedChar.index(x)) * ((len(encodedChar))**(index))

            index += 1

    ##Converte o valor em decimal para gray.
    #Converts the decimal value to gray.
    divRes = 1
    divRem = 1

    while divRes != 0:


        divRes = value // 2
        divRem = value % 2
        value = divRes

        gray.append(str(divRem))

    gray.reverse()

    ##Converte o valor em gray para binário.
    #Converts the gray value to binary.
    for i in range(0,len(gray)):
        if i == 0:

            binary.append(gray[0])

        elif gray[i] != binary[i - 1]:
            binary.append('1')
        else:
            binary.append('0')

    binary.reverse()

    ##Converte o valor em gray para decimal.
    #Converts the gray value to decimal
    value = 0
    for i in range (0, len(binary)):
        value += int(binary[i]) * (2**(i))


    ##Converte o valor decimal para caractere usando seus valores de index.
    #Converts the decimal value to characters using their index values.
    divRes = 1
    divRem = 1

    while divRes != 0:

        divRes = value // (len(encodedChar))
        divRem = value % (len(encodedChar))
        value = divRes

        codList.append(encodedChar[divRem])

    codList.reverse()

    ##Une os caracteres codificados em uma string.
    #Unites the codified characters into a string.
    for i in codList:
        cod += i

    ##Mostra a string codificada.
    #Prints the encoded string.
    print('\nA sequência de caracteres codificadas é: ' + cod)

    ##Pergunta se o usuário quer codificar outra string.
    #Asks if the user wants to encode another string.
    again = input('\nInsira 1 se você gostaria de codificar ou decodificar outra sequência de caracteres: ')
    
    if again == '1':
        choice()

def choice():
    print('Você quer codificar ou decodificar uma string?\n')
    print('1. Codificar')
    print('2. Decodificar\n')

    choice = input()

    if choice == '1':
        encoder()
    elif choice == '2':
        decoder()

choice()