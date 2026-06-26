import pandas as pd
import numpy as np

from Transacao import Transacao, TipoTransacao
from MetaMensal import MetaMensal
from ContaBancaria import ContaBancaria

class GerenciadorFinanceiro:
    def __init__(self, conta:ContaBancaria):
        self.lista_transacoes = []
        self.lista_metas = []
        self.conta = conta

    #não preciso falar o que isso faz
    def calcularSaldoGeral(self, transacao: Transacao):
        if transacao.tipo == 'receita':
            self.conta.saldo += transacao.valor
        else:
            self.conta.saldo -= transacao.valor
    
    # adiciona uma transacao recente no historico
    def addTransacao(self, transacao: Transacao):
        self.lista_transacoes.append(transacao)
        self.calcularSaldoGeral(transacao)
    
    #adiciona uma nova meta na lista
    def addMeta(self, meta:MetaMensal):
        self.lista_metas.append(meta)
    