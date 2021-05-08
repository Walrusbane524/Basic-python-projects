# Recebe n do usuário, calcula e imprime os primeiros n elementos da sequência Fibonacci
# Receives n from the user, then calculates and prints the first n elements from the Fibonacci sequence

n = int(input('Insira o número de elementos da sequência de Fibonacci que deseja: '))
print('\n\n')
x = 1
y = x

#Mostra 20 números da Sequência de Fibonacci
for cont in range (1, n + 1):
    
    #Pula uma iteração só para repetir o número inicial
    if cont > 2:
        
        #Calcula o próximo número da sequência
        x += y
        y = x - y
     
    #Imprime o número 
    print(x)