# coding=utf-8
minha_variavel = 'Olá Mundo'

for letra in minha_variavel:
    print(letra)

lista = [0,1,2,3,4,5,6,7,8,9,10]
print(range(11))

# numero ímpares
print(range(1,10,2))

# numeros pares
numeros_pares = range(0,11,2)

for numero in numeros_pares:
    print(numero ** 2)

# While
x = 0
while x <= 10:
    print(x ** 2)
    x += 2 #increment while

usuario_quiser = True

while usuario_quiser:
    print("Continue")
    usuario_quiser = input("Deseja continuar?")
    