from enum import Enum

class TipoTransacao(Enum):
    RECEITA = "receita"
    DESPESA = "despesa"

class Transacao:
    #só a criação do construtor bem simples
    # categoria diz se é essencial, lazer,  alimentação
    def __init__(self, data, descricao, valor, tipo: TipoTransacao, categoria):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria