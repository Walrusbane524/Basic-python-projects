# Recebe os coeficientes do usuário, calcula e verifica o valor de delta, calcula o 
# valor das raízes e imprime-as

# Receives the coefficients from the user, calculates and checks the value of delta, 
# then calculates the value of the roots and prints them

print('Bem-vindo ao solucionador de equações de segundo grau! \n\n')

# Recebe os coeficientes do usuário.
# Receives the coefficients from the user
a = int(input('Insira o primeiro coeficiente: '))
b = int(input('Insira o segundo coeficiente: '))
c = int(input('Insira o terceiro coeficiente: '))

delta = b**2 + ((-4)*a*c)

# Se o delta for positivo, ambas as raízes são calculadas e impressas.
# If delta is positive, both roots are calculated and printed
if delta > 0:

    print('\n\nEssa equação possui duas raízes reais e diferentes!\n')
    
    x1 = (-b + delta**(0.5))/2*a
    x2 = (-b - delta**(0.5))/2*a
    
    print('A primeira raiz é:', x1)
    print('A segunda raiz é:', x2)

# Se o delta for nulo, a raiz será calculada e impressa.
# If delta is 0, the single root will be calculated and printed.
elif delta == 0:

    print('\n\nEssa equação só possui uma raiz real!\n')
    
    x = (-b)/(2*a)
    
    print('A raiz é', x)

# Se o delta for negativo, o usuário será avisado de que a equação não possui raízes reais.
# If the delta is negative, the user will be warned that the equation has no real roots.
else:
    
    print('\n\nEsta equação não possui raízes reais!')