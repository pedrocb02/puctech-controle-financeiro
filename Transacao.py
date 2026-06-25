class Transacao:

    #só a criação do construtor bem simples
    def __init__(self, data, descricao, valor, tipo, categoria):
        self.data = data #data da sua transacao
        self.descricao = descricao #descricao da transacao
        self.valor = valor #valor transitado, ganhou ou gasto 
        self.tipo = tipo #se e receita(receber) ou gasto(dispesa)
        self.categoria = categoria # categoria diz se é essencial, lazer,  alimentação 

    def __str__(self):
        return str(self.__dict__)