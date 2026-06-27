import streamlit as st
from datetime import date

from ContaBancaria import ContaBancaria
from GerenciadorFinanceiro import GerenciadorFinanceiro
from MetaMensal import MetaMensal
from Transacao import Transacao, TipoTransacao


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

        descricao = st.text_input("Descrição / Categoria")
        valor = st.number_input("Valor", min_value=0.01, step=0.01)
        data_transacao = st.date_input("Data", value=date.today())

        tipo_escolhido = st.selectbox(
            "Tipo",
            ["Receita", "Despesa"]
        )

        if st.button("Salvar"):
            if descricao.strip() == "":
                st.error("Digite uma descrição.")
            else:
                if tipo_escolhido == "Receita":
                    tipo = TipoTransacao.RECEITA
                else:
                    tipo = TipoTransacao.DESPESA

                nova_transacao = Transacao(
                    data_transacao,
                    descricao.strip(),
                    valor,
                    tipo
                )

                gerenciador.addTransacao(nova_transacao)

                st.success("Transação cadastrada com sucesso!")
                st.rerun()

    elif opcao == "Histórico":
        st.header("Histórico")

        if len(gerenciador.lista_transacoes) == 0:
            st.info("Nenhuma transação cadastrada.")
        else:
            filtro = st.selectbox(
                "Filtrar",
                ["Todas", "Receitas", "Despesas"]
            )

            for transacao in gerenciador.lista_transacoes:
                mostrar = False

                if filtro == "Todas":
                    mostrar = True
                elif filtro == "Receitas" and transacao.tipo == TipoTransacao.RECEITA:
                    mostrar = True
                elif filtro == "Despesas" and transacao.tipo == TipoTransacao.DESPESA:
                    mostrar = True

                if mostrar:
                    if transacao.tipo == TipoTransacao.RECEITA:
                        sinal = "+"
                        tipo_texto = "Receita"
                    else:
                        sinal = "-"
                        tipo_texto = "Despesa"

                    st.write(
                        f"{transacao.data} | "
                        f"{transacao.descricao} | "
                        f"{tipo_texto} | "
                        f"{sinal} R$ {transacao.valor:.2f}"
                    )

    elif opcao == "Metas":
        st.header("Metas mensais")

        st.subheader("Criar nova meta")

        valor_meta = st.number_input("Valor da meta", min_value=0.01, step=0.01)
        mes_ano = st.text_input("Mês/Ano", placeholder="Ex: 06/2026")

        if st.button("Criar meta"):
            if mes_ano.strip() == "":
                st.error("Digite o mês e o ano.")
            else:
                nova_meta = MetaMensal(valor_meta, mes_ano.strip())
                gerenciador.addMeta(nova_meta)

                st.success("Meta criada com sucesso!")
                st.rerun()

        st.divider()

        st.subheader("Metas cadastradas")

        if len(gerenciador.lista_metas) == 0:
            st.info("Nenhuma meta cadastrada.")
        else:
            for i, meta in enumerate(gerenciador.lista_metas):
                st.write(f"### Meta {i + 1}")

                st.write(f"Mês/Ano: {meta.mes_ano}")
                st.write(f"Valor alvo: R$ {meta.valor_alvo:.2f}")
                st.write(f"Guardado: R$ {meta.montante:.2f}")
                st.write(f"Falta: R$ {meta.getFaltaQuanto():.2f}")

                progresso = meta.montante / meta.valor_alvo

                if progresso > 1:
                    progresso = 1

                st.progress(progresso)

                if meta.montante >= meta.valor_alvo:
                    st.success("Meta atingida!")

                st.write("Movimentar meta:")

                valor_guardar = st.number_input(
                    f"Valor para guardar na meta {i + 1}",
                    min_value=0.01,
                    step=0.01,
                    key=f"guardar_{i}"
                )

                if st.button(f"Guardar na meta {i + 1}", key=f"btn_guardar_{i}"):
                    if valor_guardar > conta.saldo:
                        st.error("Você não tem saldo suficiente para guardar esse valor.")
                    else:
                        entrada = Transacao(
                            date.today(),
                            f"Guardado na meta {meta.mes_ano}",
                            valor_guardar,
                            TipoTransacao.DESPESA
                        )

                        meta.engordarVacaquinha(conta, entrada)

                        st.success("Valor guardado na meta!")
                        st.rerun()

                valor_retirar = st.number_input(
                    f"Valor para retirar da meta {i + 1}",
                    min_value=0.01,
                    step=0.01,
                    key=f"retirar_{i}"
                )

                if st.button(f"Retirar da meta {i + 1}", key=f"btn_retirar_{i}"):
                    if valor_retirar > meta.montante:
                        st.error("Essa meta não tem esse valor guardado.")
                    else:
                        saida = Transacao(
                            date.today(),
                            f"Retirado da meta {meta.mes_ano}",
                            valor_retirar,
                            TipoTransacao.RECEITA
                        )

                        meta.emagrecerVaquinha(conta, saida)

                        st.success("Valor retirado da meta!")
                        st.rerun()

                st.divider()

    elif opcao == "Gráficos":
        st.header("Gráficos")
        st.info("Tela de gráficos em desenvolvimento.")


if __name__ == "__main__":
    rodar_gui()