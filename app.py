import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Meu Financeiro",
    page_icon="💸",
    layout="wide"
)

# ==========================================
# CSS PREMIUM
# ==========================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp {
    background-color: #0B1020;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#111827,#0F172A);
}

/* Títulos */
h1,h2,h3,h4,h5,h6 {
    color:white !important;
}

/* Texto */
p,label,span,div {
    color:#E5E7EB !important;
}

/* KPIs */
[data-testid="metric-container"]{
    background:#111827;
    border:1px solid #1F2937;
    border-radius:18px;
    padding:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.30);
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea {
    background:#1F2937 !important;
    color:white !important;
    border-radius:10px !important;
}

/* Botões */
.stButton button{
    background:linear-gradient(90deg,#2563EB,#3B82F6);
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    height:48px;
}

/* Separador */
hr{
    border-color:#334155;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOGIN
# ==========================================

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:

    c1,c2,c3 = st.columns([1,2,1])

    with c2:

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.title("💸 Meu Financeiro")

        st.caption("Painel Financeiro Executivo")

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):

            if usuario == "felipe" and senha == "123456":

                st.session_state.logado = True
                st.rerun()

            else:

                st.error("Usuário ou senha inválidos")

# ==========================================
# SISTEMA
# ==========================================

else:

    with st.sidebar:

        st.markdown("## 💸 Meu Financeiro")

        pagina = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Receitas",
                "Despesas",
                "Cartões",
                "Contas",
                "Relatórios",
                "Configurações"
            ],
            icons=[
                "house",
                "cash-stack",
                "wallet2",
                "credit-card",
                "bank",
                "bar-chart",
                "gear"
            ],
            default_index=0,
            styles={
                "container": {
                    "background-color":"#111827"
                },
                "icon": {
                    "color":"#60A5FA"
                },
                "nav-link": {
                    "font-size":"15px",
                    "border-radius":"10px",
                    "color":"white"
                },
                "nav-link-selected": {
                    "background-color":"#2563EB"
                }
            }
        )

    # ======================================
    # DASHBOARD
    # ======================================

    if pagina == "Dashboard":

        st.title("Dashboard Executivo")

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.metric(
                "Saldo Atual",
                "R$ 15.200",
                "+12%"
            )

        with c2:
            st.metric(
                "Receitas",
                "R$ 20.500",
                "+8%"
            )

        with c3:
            st.metric(
                "Despesas",
                "R$ 5.300",
                "-2%"
            )

        with c4:
            st.metric(
                "Resultado",
                "R$ 15.200"
            )

        st.divider()

        st.subheader("Evolução Financeira")

        grafico = {
            "Jan":5000,
            "Fev":6500,
            "Mar":8200,
            "Abr":9800,
            "Mai":12100,
            "Jun":15200
        }

        st.line_chart(grafico)

        st.divider()

        st.subheader("Últimos Lançamentos")

        st.dataframe(
            [
                {
                    "Data":"09/10/2026",
                    "Tipo":"Receita",
                    "Descrição":"Salário",
                    "Valor":"R$ 8.500"
                },
                {
                    "Data":"08/10/2026",
                    "Tipo":"Despesa",
                    "Descrição":"Mercado",
                    "Valor":"R$ 350"
                }
            ],
            use_container_width=True
        )

    elif pagina == "Receitas":

        st.title("💰 Receitas")

        st.date_input("Data")

        st.text_input("Descrição")

        st.selectbox(
            "Categoria",
            [
                "Salário",
                "Freelance",
                "Comissão",
                "Outros"
            ]
        )

        st.number_input(
            "Valor",
            min_value=0.0
        )

        st.button("Salvar Receita")

    elif pagina == "Despesas":

        st.title("💸 Despesas")

        st.date_input("Data")

        st.text_input("Descrição")

        st.selectbox(
            "Categoria",
            [
                "Moradia",
                "Mercado",
                "Lazer",
                "Combustível",
                "Outros"
            ]
        )

        st.number_input(
            "Valor",
            min_value=0.0
        )

        st.text_area("Observação")

        st.button("Salvar Despesa")

    elif pagina == "Cartões":

        st.title("💳 Cartões")

        st.text_input("Nome do Cartão")
        st.number_input("Limite", min_value=0.0)
        st.button("Salvar Cartão")

    elif pagina == "Contas":

        st.title("🏦 Contas")

        st.text_input("Nome da Conta")
        st.number_input("Saldo Inicial", min_value=0.0)
        st.button("Salvar Conta")

    elif pagina == "Relatórios":

        st.title("📈 Relatórios")
        st.info("Módulo em construção")

    elif pagina == "Configurações":

        st.title("⚙️ Configurações")

        st.text_input("Novo Usuário")

        st.text_input(
            "Nova Senha",
            type="password"
        )

        st.button("Salvar")