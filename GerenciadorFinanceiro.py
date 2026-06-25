import pandas as pd
import numpy as np

from Transacao import Transacao
from MetaMensal import MetaMensal

class GerenciadorFinanceiro:
    def __init__(self):
        self.lista_transacoes = []
        self.lista_metas = []