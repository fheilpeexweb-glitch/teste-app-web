import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="❤️ Dois Corações",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

footer {
    visibility:hidden;
}

.stApp{
    background-color:#0B1020;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#0F172A);
}

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

p,label,span,div{
    color:#E5E7EB !important;
}

[data-testid="metric-container"]{
    background:#111827;
    border:1px solid #1F2937;
    border-radius:18px;
    padding:20px;
}

.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea{
    background:#1F2937 !important;
    color:white !important;
    border-radius:10px !important;
}

.stButton button{
    background:linear-gradient(90deg,#DC2626,#EF4444);
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    height:48px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOGIN
# ==========================================

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        st.title("❤️ Dois Corações")
        st.caption("Gestão Inteligente da Marmitaria")

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):

            if usuario == "felipe" and senha == "123456":

                st.session_state.logado = True
                st.rerun()

            else:
                st.error("Usuário ou senha inválidos")

        st.markdown("---")

        if st.button("🔐 Esqueci minha senha"):

            st.info(
                "Informe seu e-mail na próxima versão para recuperação de senha."
            )

# ==========================================
# SISTEMA
# ==========================================

else:

    with st.sidebar:

        st.markdown("## ❤️ Dois Corações")
        st.caption("Marmitaria")

        pagina = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Pedidos",
                "Financeiro",
                "Relatórios",
                "Configurações"
            ],
            icons=[
                "house",
                "basket",
                "cash-stack",
                "bar-chart",
                "gear"
            ],
            default_index=0,
            styles={
                "container":{
                    "background-color":"#111827"
                },
                "icon":{
                    "color":"#F87171"
                },
                "nav-link":{
                    "font-size":"15px",
                    "border-radius":"10px"
                },
                "nav-link-selected":{
                    "background-color":"#DC2626"
                }
            }
        )

    # =====================================
    # DASHBOARD
    # =====================================

    if pagina == "Dashboard":

        st.title("❤️ Dashboard")

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.metric(
                "🍱 Marmitas Hoje",
                "58"
            )

        with c2:
            st.metric(
                "💵 Faturamento",
                "R$ 1.850"
            )

        with c3:
            st.metric(
                "💸 Despesas",
                "R$ 620"
            )

        with c4:
            st.metric(
                "📈 Lucro",
                "R$ 1.230"
            )

        st.divider()

        st.subheader("📊 Vendas da Semana")

        st.bar_chart({
            "Seg":18,
            "Ter":22,
            "Qua":20,
            "Qui":25,
            "Sex":30,
            "Sab":15
        })

        st.divider()

        st.subheader("📈 Evolução do Faturamento")

        st.line_chart({
            "Jan":15000,
            "Fev":18000,
            "Mar":21000,
            "Abr":25000,
            "Mai":27000,
            "Jun":31000
        })

    # =====================================
    # PEDIDOS
    # =====================================

    elif pagina == "Pedidos":

        st.title("🍱 Pedidos")

        cliente = st.text_input("Cliente")

        telefone = st.text_input("Telefone")

        quantidade = st.number_input(
            "Quantidade",
            min_value=1
        )

        produto = st.selectbox(
            "Produto",
            [
                "Marmita Pequena",
                "Marmita Média",
                "Marmita Grande"
            ]
        )

        valor = st.number_input(
            "Valor",
            min_value=0.0
        )

        status = st.selectbox(
            "Status",
            [
                "Recebido",
                "Produzindo",
                "Entregue",
                "Cancelado"
            ]
        )

        st.button("Salvar Pedido")

    # =====================================
    # FINANCEIRO
    # =====================================

    elif pagina == "Financeiro":

        st.title("💰 Financeiro")

        tipo = st.selectbox(
            "Tipo",
            [
                "Receita",
                "Despesa"
            ]
        )

        data = st.date_input("Data")

        descricao = st.text_input("Descrição")

        valor = st.number_input(
            "Valor",
            min_value=0.0
        )

        observacao = st.text_area(
            "Observação"
        )

        st.button("Salvar")

    # =====================================
    # RELATÓRIOS
    # =====================================

    elif pagina == "Relatórios":

        st.title("📈 Relatórios")

        st.info(
            "Em breve: faturamento, despesas e lucro detalhados."
        )

    # =====================================
    # CONFIGURAÇÕES
    # =====================================

    elif pagina == "Configurações":

        st.title("⚙️ Configurações")

        st.text_input("E-mail de recuperação")

        st.text_input(
            "Nova Senha",
            type="password"
        )

        st.button("Salvar Configurações")