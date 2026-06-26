import streamlit as st
from datetime import date
from Transacao import Transacao, TipoTransacao
from ContaBancaria import ContaBancaria
from GerenciadorFinanceiro import GerenciadorFinanceiro

# ── configuração da página ──────────────────────────────────────────
st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="centered")

st.markdown("""
<style>
    .metric-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        border: 1px solid #e9ecef;
    }
    .metric-value { font-size: 1.8rem; font-weight: 600; margin: 0; }
    .metric-label { font-size: 0.8rem; color: #6c757d; margin: 0; text-transform: uppercase; letter-spacing: 0.05em; }
    .green { color: #2d9e6b; }
    .red   { color: #d94f3d; }
    .gray  { color: #495057; }
    .divider { border: none; border-top: 1px solid #e9ecef; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── estado da sessão (persiste enquanto o app está aberto) ──────────
if "gerenciador" not in st.session_state:
    conta = ContaBancaria("Minha conta", saldo_inicial=0.0)
    st.session_state.gerenciador = GerenciadorFinanceiro(conta)

gerenciador = st.session_state.gerenciador
conta = gerenciador.conta

# ── cabeçalho ───────────────────────────────────────────────────────
col_titulo, col_salvar = st.columns([4, 1])
with col_titulo:
    st.title("Controle Financeiro")
    st.caption(f"Conta: {conta.nome}")


# ── métricas no topo ────────────────────────────────────────────────
receitas = sum(t.valor for t in conta.historico_transacoes if t.tipo == TipoTransacao.RECEITA)
despesas = sum(t.valor for t in conta.historico_transacoes if t.tipo == TipoTransacao.DESPESA)

col1, col2, col3 = st.columns(3)

with col1:
    cor = "green" if conta.saldo >= 0 else "red"
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-label">Saldo atual</p>
        <p class="metric-value {cor}">R$ {conta.saldo:,.2f}</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-label">Receitas</p>
        <p class="metric-value green">R$ {receitas:,.2f}</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-label">Despesas</p>
        <p class="metric-value red">R$ {despesas:,.2f}</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── formulário de nova transação ─────────────────────────────────────
st.subheader("Nova transação")

with st.form("form_transacao", clear_on_submit=True):
    col_a, col_b = st.columns(2)
    with col_a:
        descricao = st.text_input("Descrição", placeholder="ex: Almoço, Salário...")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f")
    with col_b:
        tipo = st.selectbox("Tipo", ["Receita", "Despesa"])
        data = st.date_input("Data", value=date.today())

    salvar = st.form_submit_button("Adicionar transação", use_container_width=True)

    if salvar:
        if not descricao.strip():
            st.error("Preencha a descrição.")
        else:
            tipo_enum = TipoTransacao.RECEITA if tipo == "Receita" else TipoTransacao.DESPESA
            t = Transacao(data, descricao.strip(), valor, tipo_enum)
            gerenciador.addTransacao(t)
            st.success(f"{'Receita' if tipo == 'Receita' else 'Despesa'} de R$ {valor:,.2f} adicionada!")
            st.rerun()

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── histórico de transações ──────────────────────────────────────────
st.subheader("Histórico")

historico = conta.historico_transacoes

if not historico:
    st.info("Nenhuma transação registrada ainda. Adicione a primeira acima!")
else:
    filtro = st.selectbox("Filtrar por tipo", ["Todos", "Receitas", "Despesas"], label_visibility="collapsed")

    lista = historico
    if filtro == "Receitas":
        lista = [t for t in historico if t.tipo == TipoTransacao.RECEITA]
    elif filtro == "Despesas":
        lista = [t for t in historico if t.tipo == TipoTransacao.DESPESA]

    if not lista:
        st.info(f"Nenhuma {filtro.lower()[:-1]} encontrada.")
    else:
        for t in reversed(lista):
            sinal = "+" if t.tipo == TipoTransacao.RECEITA else "-"
            cor_tag = "green" if t.tipo == TipoTransacao.RECEITA else "red"
            data_fmt = t.data.strftime("%d/%m/%Y") if hasattr(t.data, "strftime") else str(t.data)

            col_desc, col_val = st.columns([3, 1])
            with col_desc:
                st.markdown(f"**{t.descricao}** &nbsp; <span style='color:#6c757d;font-size:.85rem'>{data_fmt}</span>", unsafe_allow_html=True)
            with col_val:
                st.markdown(f"<p style='text-align:right;font-weight:600' class='{cor_tag}'>{sinal} R$ {t.valor:,.2f}</p>", unsafe_allow_html=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

        # gráfico de barras receitas x despesas
        if receitas > 0 or despesas > 0:
            st.subheader("Visão geral")
            st.bar_chart({"Receitas": receitas, "Despesas": despesas})

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.subheader("Distribuição dos gastos")

        df_gastos = gerenciador.getDistribuicaoGastos()

        if df_gastos is None:
            st.info("Nenhuma despesa registrada ainda.")
        else:
            st.bar_chart(df_gastos)