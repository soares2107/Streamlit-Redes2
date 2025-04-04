import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("📈 Previsão de Nota com Regressão Linear")

st.markdown("Preveja sua próxima nota com base nas **horas de estudo** e **nota anterior**.")

# Entradas do usuário
horas_estudo = st.number_input("Horas de Estudo (por semana)", min_value=0.0, step=0.5)
nota_anterior = st.slider("Nota anterior", 0.0, 10.0, 5.0)

# Dados de exemplo (mock)
# Supondo que essas sejam observações anteriores
X = np.array([
    [1, 3], [2, 4], [3, 5], [4, 6],
    [5, 5], [6, 6.5], [7, 7], [8, 7.5],
    [9, 8], [10, 9],
    [5, 4], [7, 5.5], [3, 6], [2, 7], [4, 8],
])

y = np.array([
    4, 5, 5.5, 6,
    6, 7, 7.5, 7,
    8, 9,
    5, 6, 6.5, 7, 8
])


# Treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão com base nos inputs
entrada = np.array([[horas_estudo, nota_anterior]])
previsao = modelo.predict(entrada)[0]
previsao = max(0, min(previsao, 10))  # garante que a nota fique entre 0 e 10


st.subheader("📊 Previsão da Próxima Nota:")
st.success(f"Sua nota prevista é **{previsao:.2f}**")

# Gráfico de comparação
st.subheader("📉 Visualização do Modelo")

fig, ax = plt.subplots()
ax.scatter(X[:, 0], y, color='blue', label='Histórico (Horas x Nota)')
ax.scatter(horas_estudo, previsao, color='red', label='Sua previsão')
ax.set_xlabel("Horas de Estudo")
ax.set_ylabel("Nota")
ax.legend()
st.pyplot(fig)
