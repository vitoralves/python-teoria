# coding= utf-8

devo_continuar = False

if devo_continuar:
    print("continue")

pessoas_conhecidas = ['João', 'Maria', 'Ana', 'Fábio']
pessoa = input("Entre com o nome de uma pessoa:")

# if pessoa in pessoas_conhecidas:
#     print("Você conhece "+ pessoa)

# if pessoa not in pessoas_conhecidas:
#     print("Você não conhece "+pessoa)

if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa))
else:
    print("Você não conhece {}".format(pessoa))