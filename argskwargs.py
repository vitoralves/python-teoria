def soma_simples(*args):
    return sum(args)

print(soma_simples(1,5,10,90))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

metodo_kwargs(3, 'vitor', 5, 'qualquer', nome='Vitor', idade=24)