# Projeto simples que recebe um número x pelo input do usuário e imprime o mesmo, sua metade, 
# seu dobro, seu quadrado, sua raiz quadrada, ele elevado a ele mesmo e sua x-ésima raiz.

# Simple project that receives a number x as user input and prints itself, its half, its double
# itself squared, its square root, it raised to the power of itself and its xth root.

x = int(input('Insira um número inteiro: \n'))

print(x)
print(x/2)
print(x*2)
print(x**2)
print(x**(1/2))
print(x**x)
print(x**(1/x))