import streamlit as st
import pandas as pd
import numpy as np

st.title("📋 Filtro Dinâmico em Tabela")

# Gerar dados fictícios
np.random.seed(42)
cidades = ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Curitiba', 'Goiania']
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros']

df = pd.DataFrame({
    'Cidade': np.random.choice(cidades, 200),
    'Categoria': np.random.choice(categorias, 200),
    'Preço': np.round(np.random.uniform(10, 500, 200), 2),
    'Quantidade': np.random.randint(1, 20, 200)
})

st.subheader("Filtros")

# Filtros categóricos
cidade_filtro = st.multiselect("Filtrar por cidade:", options=df['Cidade'].unique(), default=df['Cidade'].unique())
categoria_filtro = st.multiselect("Filtrar por categoria:", options=df['Categoria'].unique(), default=df['Categoria'].unique())

# Filtro numérico (slider)
preco_min, preco_max = st.slider("Filtrar por faixa de preço:", 
                                 float(df['Preço'].min()), 
                                 float(df['Preço'].max()), 
                                 (float(df['Preço'].min()), float(df['Preço'].max())))

# Aplicar filtros
df_filtrado = df[
    (df['Cidade'].isin(cidade_filtro)) &
    (df['Categoria'].isin(categoria_filtro)) &
    (df['Preço'] >= preco_min) & (df['Preço'] <= preco_max)
]

st.subheader("Tabela Filtrada")
st.dataframe(df_filtrado)
