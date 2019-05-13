# coding=utf-8
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print("****Embrulhando função do decorador****")
        funcao()
        print("*****Fim embrulho*******")
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print('Eu sou uma função')

minha_funcao()