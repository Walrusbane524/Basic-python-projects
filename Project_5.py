# Recebe o dia, mês e ano (meses neste programa só têm 30 dias) inicial e final, calcula e imprime a 
# diferença de dias. 

# Receives the starting and last days, months and years (in this program all months have 30 days),
# calculates and prints the difference in days.

dia1 = int(input('Insira o dia inicial: '))
mes1 = int(input('Insira o mês inicial: '))
ano1 = int(input('Insira o ano inicial: '))

dia2 = int(input('Insira o dia final: '))
mes2 = int(input('Insira o mês final: '))
ano2 = int(input('Insira o ano final: '))

dias_restantes = ((ano2 * 360) + (mes2 * 30) + dia2) - ((ano1 * 360) + (mes1* 30) + dia1)

print('Dias restantes: ' + str(dias_restantes))