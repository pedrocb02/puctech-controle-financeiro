from Transacao import Transacao, TipoTransacao
from MetaMensal import MetaMensal
from ContaBancaria import ContaBancaria
import pandas as pd

class GerenciadorFinanceiro:
    def __init__(self, conta:ContaBancaria):
        self.lista_transacoes = []
        self.lista_metas = []
        self.conta = conta

    #não preciso falar o que isso faz
    def addTransacao(self, transacao: Transacao):
        self.lista_transacoes.append(transacao)
        self.conta.registrar_transacao(transacao)
        
    #adiciona uma nova meta na lista
    def addMeta(self, meta:MetaMensal):
        self.lista_metas.append(meta)

    def __str__(self):

        texto = (
            f"\n{'=' * 50}\n"
            f"GERENCIADOR FINANCEIRO\n"
            f"{'=' * 50}\n"
            f"Nome da Conta: {self.conta.nome}\n"
            f"Saldo Atual: R$ {self.conta.saldo:.2f}\n"
            f"{'=' * 50}\n\n"
        )

        # Metas
        texto += "METAS MENSAIS\n"
        texto += "-" * 50 + "\n"

        if len(self.lista_metas) == 0:
            texto += "Nenhuma meta cadastrada.\n"
        else:
            for i, meta in enumerate(self.lista_metas, start=1):
                texto += f"Meta {i}: {meta}\n"

        texto += "\n"

        # Transações
        texto += "HISTÓRICO DE TRANSAÇÕES\n"
        texto += "-" * 50 + "\n"

        if len(self.lista_transacoes) == 0:
            texto += "Nenhuma transação cadastrada.\n"
        else:
            for i, transacao in enumerate(self.lista_transacoes, start=1):
                texto += f"Transação {i}: {transacao}\n"

        texto += "=" * 50

        return texto
    
    def getDistribuicaoGastos(self):
        dados = [
            {"Categoria": t.descricao, "Valor": t.valor}
            for t in self.lista_transacoes
            if t.tipo == TipoTransacao.DESPESA
        ]
        if not dados:
            return None
        df = pd.DataFrame(dados)
        return df.groupby("Categoria")["Valor"].sum().sort_values(ascending=False)