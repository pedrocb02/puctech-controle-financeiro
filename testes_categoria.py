from Transacao import Transacao, TipoTransacao
from ContaBancaria import ContaBancaria
from GerenciadorFinanceiro import GerenciadorFinanceiro

conta = ContaBancaria("Minha conta")
gerente = GerenciadorFinanceiro(conta)

# transacoes de exemplo
gerente.addTransacao(Transacao("2023-10-01", "Salário", 5000, TipoTransacao.RECEITA, "trabalho"))
gerente.addTransacao(Transacao("2023-10-05", "Aluguel", 1500, TipoTransacao.DESPESA, "moradia"))
gerente.addTransacao(Transacao("2023-10-10", "Supermercado", 300, TipoTransacao.DESPESA, "alimentação"))
gerente.addTransacao(Transacao("2023-10-15", "Cinema", 50, TipoTransacao.DESPESA, "lazer"))
gerente.addTransacao(Transacao("2023-10-20", "ifood", 100, TipoTransacao.DESPESA, "alimentação"))

gerente.gastos_por_categoria()
print(f"Saldo atual: R$ {conta.saldo:.2f}")