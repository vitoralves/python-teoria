def meu_metodo():
    print("Hello World")
    print("Novo print")
    print("Sem identacao")

# meu_metodo()

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

# print(soma_dois_valores(2, 10))

notas = [3,5,6,4,10]
notas.append(8)
notas.append(7)
notas.append(1)

print(notas)
print(len(notas))
print(sum(notas)/len(notas))