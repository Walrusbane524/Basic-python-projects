# Recebe o nome e dia do mês do usuário e imprime um olá, o dia anterior e posterior ao dado.
# Receives the user name and day of month and prints a hello, the day before and the day after the given one.

nome = str(input('Insira o seu nome: '))
dia = int(input('Insira o dia do mês de hoje: '))

print('Olá, ' + nome)
print('Ontem foi ' + str(dia - 1))
print('Hoje é ' + str(dia))
print('Amanhã será ' + str(int(dia) + 1))