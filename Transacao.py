class Transacao:

    #só a criação do construtor bem simples
    # categoria diz se é essencial, lazer,  alimentação
    def __init__(self, data, descricao, valor, tipo, categoria):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria

