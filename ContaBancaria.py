from Transacao import TipoTransacao
class ContaBancaria:
    def __init__(self, nome, saldo_inicial = 0.0):
        self.nome = nome
        self.saldo = float(saldo_inicial)
        self.historico_transacoes = []# Transações que aconteceram na conta

    def registrar_transacao(self, transacao):
        self.historico_transacoes.append(transacao)
        
        # Atualiza o saldo da conta na hora que a transação é adicionada
        if transacao.tipo == TipoTransacao.RECEITA:
            self.saldo += transacao.valor
        else:
            self.saldo -= transacao.valor
