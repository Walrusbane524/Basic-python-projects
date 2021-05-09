# Recebe os coeficientes de uma equação de primeiro grau do usuário, calcula e imprime a sua raiz.
# Receives the coefficients from the user, calculates and prints the root.

a = float(input('Insira o coeficiente angular da equação: '))
b = float(input('Insira o coeficiente linear da equação: '))

raiz = (-b)/a

print('A raiz desta equação é ' + (str(raiz)))