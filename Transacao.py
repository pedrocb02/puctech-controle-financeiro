from enum import Enum

class TipoTransacao(Enum):
    RECEITA = "receita"
    DESPESA = "despesa"

class Transacao:
    def __init__(self, data, descricao, valor, tipo: TipoTransacao, categoria):
        self.data = data
        self.descricao = descricao
        self.valor = float(valor)
        self.tipo = tipo
        self.categoria = categoria

    def __str__(self):
      return str(self.__dict__)