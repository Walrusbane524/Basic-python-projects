# Recebe 3 variáveis lógicas do usuário e calcula uma série de operações de "e" e "ou" lógicos.
# Receives 3 logic variables from the user and calculates a bunch of logic "and" and "or" operations.

a = bool(input('Insira o primeiro valor lógico: '))
b = bool(input('Insira o segundo valor lógico: '))
c = bool(input('Insira o terceiro valor lógico: '))

print('a e b: ' + str(a and b))
print('a e c: ' + str(a and c))
print('b ou c: '+ str(b or c))
print('a e b e c: ' + str(a and b and c))
print('contrário de a ou b: ' + str((not a) or b))
print('contrário de a ou contrário de b: ' + str((not a) or (not c)))
print('(contrário de a ou b) e c' + str(((not a) or b) and c))
print('contrário de a e contrário de b e contrário de c: ' + str((not a) and (not b) and (not c)))
print('contrário de (a ou b ou c): ' + str(not (a or b or c)))
print('a e falso: ' + str(a and False))
print('a e contrário de a: ' + str(a and (not a)))
print('a ou contrário de a: ' + str(a or (not a)))