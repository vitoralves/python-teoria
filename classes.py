class JogadorLoteria:
    def __init__(self):
        self.nome = "Pedro"
        self.numeros = (13,4,52,34,90)

    def total(self):
        return sum(self.numeros)

jogador1 = JogadorLoteria()
jogador2 = JogadorLoteria()

print(jogador1.nome)
print(jogador1.numeros)
print(jogador1.total())