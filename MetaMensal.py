from Transacao import Transacao

class MetaMensal:
    def __init__(self,  valor_alvo, mes_ano):
        self.valor_alvo = float(valor_alvo)
        self.montante = 0.0
        self.mes_ano = mes_ano

    def engordarVacaquinha(self, entrada: Transacao):
        #oqtemdentrodavaquinha
        self.montante += entrada.valor

    def emagrecerVaquinha(self, saida: Transacao):
        if saida.valor <=  self.montante:
            self.montante -= saida.valor
            return saida.valor
    
    def verificarMetaAtingida(self):
        # Retorna True atingiu a meta
        return self.montante == self.valor_alvo
    
    def getFaltaQuanto(self):
        # retorna quanto falta
        return self.valor_alvo - self.montante