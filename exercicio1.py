import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de Análise de Dados (CSV Upload)")

# Upload do CSV
uploaded_file = st.file_uploader("Faça upload do seu arquivo CSV", type=["csv"])

# Verifica se o arquivo foi enviado
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("Arquivo carregado com sucesso!")
        st.subheader("Prévia dos Dados")
        st.dataframe(df)

        # Seleciona coluna numérica
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if numeric_cols:
            col = st.selectbox("Selecione uma coluna numérica", numeric_cols)

            if col:
                media = df[col].mean()
                mediana = df[col].median()
                desvio = df[col].std()

                st.write(f"**Média:** {media:.2f}")
                st.write(f"**Mediana:** {mediana:.2f}")
                st.write(f"**Desvio Padrão:** {desvio:.2f}")

                # Gráfico interativo
                fig = px.histogram(df, x=col, nbins=30, title=f'Histograma da coluna "{col}"')
                fig.update_traces(marker_line_color='black', marker_line_width=1)
                st.plotly_chart(fig)

        else:
            st.warning("Nenhuma coluna numérica foi encontrada no arquivo.")

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

else:
    st.info("Por favor, envie um arquivo CSV para começar.")

# Mantém o estado entre ações
if "upload_status" not in st.session_state:
    st.session_state.upload_status = "Nenhum arquivo enviado ainda."
