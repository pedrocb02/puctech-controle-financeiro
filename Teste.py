import MetaMensal
import Transacao
import ContaBancaria
import GerenciadorFinanceiro



Salario = Transacao.Transacao("10/05","Tigre",599,"receita","Lazer")


#crio a conta do Daniel
Conta_Shadow_Daniel = ContaBancaria.ContaBancaria("Shadow_Daniel",0.5)


#quer comprar a XJ99 dele, Moto

Shadow_Daniel = GerenciadorFinanceiro.GerenciadorFinanceiro(Conta_Shadow_Daniel)
Shadow_Daniel.addTransacao(Salario)
print("\nGerenciador Do Saldo: ",Shadow_Daniel.conta.saldo)


Moto = MetaMensal.MetaMensal(15000,"06/2026")
Shadow_Daniel.addMeta(Moto)
print("\nMeta Moto Daniel: ",Moto)

investimento = Transacao.Transacao("26/06","Investimento pra vaca",599.5,"despesa","Lazer")

Moto.engordarVacaquinha(Conta_Shadow_Daniel,investimento)
print("\nNOVO SALDO DA VAQUINHA DANIEL: ",Moto)

print("\nGerenciamento da conta: ", Shadow_Daniel.conta.saldo)
#ta errado porque nao tirou dinheiro da conta


print(Shadow_Daniel)
