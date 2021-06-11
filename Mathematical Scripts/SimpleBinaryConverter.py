#Receives binary number as input.
#Recebe um número binário como input.
binary = input("Insira o número binário inteiro que você deseja converter para decimal:\n")

#Separates all of the characters from the binary number into a list
#Separa todos os caracteres do número binário em uma lista
digits = list(binary)
decimal = 1
i = 0

#Calculates the decimal value of the binary number using the "double-dabble" method
#Calcula o valor decimal do número binário pelo método "double-dabble"
while i <= len(digits) - 2:
  
  decimal = (decimal * 2) + int(digits[i + 1])

  i += 1

#Prints the result
#Imprime o resultado
print("O número decimal equivalente é:", decimal)