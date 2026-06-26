from Transacao import Transacao
from ContaBancaria import ContaBancaria
class MetaMensal:
    def __init__(self,  valor_alvo, mes_ano):
        self.valor_alvo = float(valor_alvo)
        self.montante = 0.0
        self.mes_ano = mes_ano

    def engordarVacaquinha(self,conta: ContaBancaria, entrada: Transacao):
        #oqtemdentrodavaquinha
        self.montante += entrada.valor
        conta.saldo -= entrada.valor

    def emagrecerVaquinha(self,conta: ContaBancaria, saida: Transacao):
        if saida.valor <=  self.montante:
            self.montante -= saida.valor
            conta.saldo += saida.valor
            
    
    def verificarMetaAtingida(self):
        # Retorna True atingiu a meta
        return self.montante == self.valor_alvo
    
    def getFaltaQuanto(self):
        # retorna quanto falta
        return self.valor_alvo - self.montante
    
    def __str__(self):
      return str(self.__dict__)