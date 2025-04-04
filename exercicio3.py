import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Simulador de Investimento com Juros Compostos")

# Entradas do usuário
valor_inicial = st.number_input("Valor inicial do investimento (R$)", min_value=0.0, value=1000.0, step=100.0)
taxa_juros = st.slider("Taxa de juros anual (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
periodo = st.selectbox("Período (anos)", options=list(range(1, 31)))

# Cálculo dos valores ao longo do tempo
anos = list(range(periodo + 1))
valores = [valor_inicial * ((1 + taxa_juros / 100) ** ano) for ano in anos]

# Criar DataFrame para o gráfico
df = pd.DataFrame({"Ano": anos, "Montante (R$)": valores})

# Cálculo final
montante_final = valores[-1]
rendimento_total = montante_final - valor_inicial

# Exibir resultados
st.subheader(f"Montante final após {periodo} anos: R$ {montante_final:,.2f}")
st.subheader(f"💹 Rendimento total no período: R$ {rendimento_total:,.2f}")

# Exibir gráfico
fig = px.line(df, x="Ano", y="Montante (R$)", title="Crescimento do Investimento")
st.plotly_chart(fig)
