import streamlit as st
import pandas as pd
import numpy as np

st.title("🗺️ Mapa Interativo com Dados Geográficos")

# Gerar dados geográficos simulados
np.random.seed(42)
cidades = [
    'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília',
    'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte',
    'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro',
    'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis',
    'São Paulo', 'Aracaju', 'Palmas'
]

categorias = ['Evento', 'Loja', 'Escola']

# Coordenadas aproximadas de cidades (latitude, longitude)
coordenadas = {
    'Rio Branco': [-9.97499, -67.8243],
    'Maceió': [-9.66599, -35.735],
    'Macapá': [0.0349, -51.0694],
    'Manaus': [-3.11903, -60.0217],
    'Salvador': [-12.9714, -38.5014],
    'Fortaleza': [-3.7172, -38.5433],
    'Brasília': [-15.7939, -47.8828],
    'Vitória': [-20.3155, -40.3128],
    'Goiânia': [-16.6869, -49.2648],
    'São Luís': [-2.5307, -44.3068],
    'Cuiabá': [-15.6014, -56.0979],
    'Campo Grande': [-20.4697, -54.6201],
    'Belo Horizonte': [-19.9167, -43.9345],
    'Belém': [-1.4558, -48.4902],
    'João Pessoa': [-7.1195, -34.845],
    'Curitiba': [-25.4284, -49.2733],
    'Recife': [-8.0476, -34.877],
    'Teresina': [-5.0892, -42.8016],
    'Rio de Janeiro': [-22.9068, -43.1729],
    'Natal': [-5.7945, -35.211],
    'Porto Alegre': [-30.0346, -51.2177],
    'Porto Velho': [-8.7608, -63.8999],
    'Boa Vista': [2.8238, -60.6753],
    'Florianópolis': [-27.5954, -48.548],
    'São Paulo': [-23.5505, -46.6333],
    'Aracaju': [-10.9472, -37.0731],
    'Palmas': [-10.2428, -48.3277]
}

# Criar dados com pequenas variações em torno das coordenadas
dados = []
for _ in range(100):
    cidade = np.random.choice(cidades)
    categoria = np.random.choice(categorias)
    lat, lon = coordenadas[cidade]
    lat += np.random.uniform(-0.02, 0.02)
    lon += np.random.uniform(-0.02, 0.02)
    dados.append({'Cidade': cidade, 'Categoria': categoria, 'Latitude': lat, 'Longitude': lon})

df = pd.DataFrame(dados)

# Filtro por categoria
categoria_filtro = st.selectbox("Filtrar por categoria:", options=['Todas'] + categorias)

# Aplicar filtro
if categoria_filtro != 'Todas':
    df = df[df['Categoria'] == categoria_filtro]

# Exibir mapa
df_mapa = df[['Latitude', 'Longitude']].rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})
st.map(df_mapa)



# Mostrar dados (opcional)
st.subheader("Dados Geográficos Filtrados")
st.dataframe(df)
