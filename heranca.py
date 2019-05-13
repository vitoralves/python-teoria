# coding: utf-8
import datetime

class Funcionario(object):
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    
    @classmethod
    def definir_novo_aumento(cls, novo_valor):
        cls.aumento = novo_valor
    
    @staticmethod
    def dia_util(dia):
        # segunda = 0
        # domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super(Admin, self).__init__(nome, salario)

    def atualizarDados(self,nome):
        self.nome = nome
        return self.dados()

vitor = Funcionario('Vitor', 1000)
print(vitor.dados())

admin = Admin('Administrador', 1000)
print(admin.nome)
print(admin.atualizarDados('Administrador Alterado'))

vitor.aplicar_aumento()
print(vitor.salario)

Funcionario.definir_novo_aumento(2)
joao = Funcionario('Joao', 4500)
joao.aplicar_aumento()
print(joao.salario)

minha_data = datetime.date(2019, 4, 11) #quinta-feira
print("Quinta-feira {}".format(Funcionario.dia_util(minha_data)))
minha_data = datetime.date(2019, 4, 14) #domingo
print("Domingo {}".format(Funcionario.dia_util(minha_data)))