import streamlit as st

from ContaBancaria import ContaBancaria
from GerenciadorFinanceiro import GerenciadorFinanceiro
from Transacao import TipoTransacao


def rodar_gui():
    st.set_page_config(
        page_title="Controle Financeiro",
        page_icon="💰",
        layout="centered"
    )

    if "gerenciador" not in st.session_state:
        conta = ContaBancaria("Minha Conta", 0)
        st.session_state.gerenciador = GerenciadorFinanceiro(conta)

    gerenciador = st.session_state.gerenciador
    conta = gerenciador.conta

    st.sidebar.title("Menu")

    opcao = st.sidebar.radio(
        "Escolha uma opção:",
        ["Adicionar transação", "Histórico", "Metas", "Gráficos"]
    )

    if st.sidebar.button("Zerar tudo"):
        st.session_state.clear()
        st.rerun()

    st.title("Controle Financeiro")
    st.write("Sistema para controlar receitas, despesas e metas mensais.")

    total_receitas = 0
    total_despesas = 0

    for transacao in gerenciador.lista_transacoes:
        if transacao.tipo == TipoTransacao.RECEITA:
            total_receitas += transacao.valor
        elif transacao.tipo == TipoTransacao.DESPESA:
            total_despesas += transacao.valor

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Saldo atual", f"R$ {conta.saldo:.2f}")

    with col2:
        st.metric("Receitas", f"R$ {total_receitas:.2f}")

    with col3:
        st.metric("Despesas", f"R$ {total_despesas:.2f}")

    st.divider()

    if opcao == "Adicionar transação":
        st.header("Adicionar transação")
        st.info("Tela de cadastro em desenvolvimento.")

    elif opcao == "Histórico":
        st.header("Histórico")
        st.info("Tela de histórico em desenvolvimento.")

    elif opcao == "Metas":
        st.header("Metas mensais")
        st.info("Tela de metas em desenvolvimento.")

    elif opcao == "Gráficos":
        st.header("Gráficos")
        st.info("Tela de gráficos em desenvolvimento.")


if __name__ == "__main__":
    rodar_gui()