from Transacao import Transacao
class MetaMensal:

    # categoria diz se é essencial, lazer, alimentação
    def __init__(self, categoria, valor_limite, mes_ano):
        self.categoria = categoria
        self.valor_limite = valor_limite
        self.mes_ano = mes_ano
    
    def metaAtingida(self, transacao):
        #retorna um TRUE ou FALSE, caso meta atingida
        return self.valor_limite >= transacao.valor
    
    def getFaltaquanto(self, transacao):
        saida = self.valor_limite - transacao.valor
        if saida >= 0:
            return saida
        else:
            return 0