import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Painel Multi-Página", layout="wide")

st.sidebar.title("📌 Navegação")
pagina = st.sidebar.radio("Escolha a página:", ["Upload de Dados", "Análise Estatística", "Gráficos Interativos"])

# Usando session_state para armazenar os dados
if 'dados' not in st.session_state:
    st.session_state.dados = None

# Página 1: Upload e visualização
if pagina == "Upload de Dados":
    st.title("📂 Upload e Visualização de Dados")

    arquivo = st.file_uploader("Envie um arquivo CSV", type="csv")

    if arquivo is not None:
        df = pd.read_csv(arquivo)
        st.session_state.dados = df  # guarda para outras páginas
        st.success("✅ Dados carregados com sucesso!")
        st.dataframe(df)

# Página 2: Análise Estatística com cache
elif pagina == "Análise Estatística":
    st.title("📊 Análise Estatística")

    if st.session_state.dados is not None:
        df = st.session_state.dados

        @st.cache_data
        def calcular_estatisticas(dados):
            return dados.describe()

        st.subheader("Resumo Estatístico")
        st.dataframe(calcular_estatisticas(df.select_dtypes(include=np.number)))
    else:
        st.warning("⚠️ Nenhum dado carregado. Vá até 'Upload de Dados' primeiro.")

# Página 3: Gráficos Interativos
elif pagina == "Gráficos Interativos":
    st.title("📈 Gráficos Interativos")

    if st.session_state.dados is not None:
        df = st.session_state.dados

        colunas_numericas = df.select_dtypes(include=np.number).columns.tolist()
        if len(colunas_numericas) >= 2:
            x = st.selectbox("Escolha a variável X", colunas_numericas)
            y = st.selectbox("Escolha a variável Y", colunas_numericas, index=1)
            tipo = st.selectbox("Tipo de gráfico", ["Dispersão (Pontos)", "Barra"])

            if tipo == "Dispersão (Pontos)":
                fig = px.scatter(df, x=x, y=y, title=f"{x} x {y}")
            elif tipo == "Barra":
                fig = px.bar(df, x=x, y=y, title=f"{x} x {y}")

            st.plotly_chart(fig)
        else:
            st.warning("O dataset precisa de pelo menos duas colunas numéricas para o gráfico.")
    else:
        st.warning("⚠️ Nenhum dado carregado. Vá até 'Upload de Dados' primeiro.")
