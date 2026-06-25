import pandas as pd
import numpy as np

from Transacao import Transacao, TipoTransacao
from MetaMensal import MetaMensal

class GerenciadorFinanceiro:
    def __init__(self):
        self.lista_transacoes = []
        self.lista_metas = []

    def addTransacao(self, transacao: Transacao):
            self.lista_transacoes.append(transacao)
    
    def calcularSaldo(self):
        saldo = 0
        for i in self.lista_transacoes:
            if(i.tipo == TipoTransacao.RECEITA):
                saldo += i.valor
            else:
                saldo -= i.valor
        return saldo