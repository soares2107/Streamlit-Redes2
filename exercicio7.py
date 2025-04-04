import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Sistema de Recomendação de Filmes com Pesos")

# Gêneros disponíveis
generos = ["Ação", "Comédia", "Drama", "Ficção Científica", "Terror", "Romance"]
preferencias = st.multiselect("📌 Escolha seus gêneros favoritos:", generos)

# Pesos por gênero
pesos_genero = {
    "Ação": 2,
    "Comédia": 1,
    "Drama": 1,
    "Ficção Científica": 2,
    "Terror": 1,
    "Romance": 1.5
}

# Lista de recomendações (28 filmes)
recomendacoes = {
    "Matrix": ["Ação", "Ficção Científica"],
    "Titanic": ["Romance", "Drama"],
    "Todo Mundo em Pânico": ["Comédia", "Terror"],
    "Vingadores": ["Ação", "Ficção Científica"],
    "Diário de uma Paixão": ["Romance", "Drama"],
    "Invocação do Mal": ["Terror"],
    "Se Beber, Não Case": ["Comédia"],
    "O Auto da Compadecida": ["Comédia", "Drama"],
    "Interestelar": ["Ficção Científica", "Drama"],
    "O Exterminador do Futuro": ["Ação", "Ficção Científica"],
    "Uma Linda Mulher": ["Romance", "Comédia"],
    "Corra!": ["Terror", "Drama"],
    "Deadpool": ["Ação", "Comédia"],
    "Gravidade": ["Ficção Científica", "Drama"],
    "Como Eu Era Antes de Você": ["Romance", "Drama"],
    "Atividade Paranormal": ["Terror"],
    "Velozes e Furiosos": ["Ação"],
    "De Repente 30": ["Comédia", "Romance"],
    "O Quinto Elemento": ["Ação", "Ficção Científica"],
    "A Chegada": ["Ficção Científica", "Drama"],
    "It: A Coisa": ["Terror"],
    "A Proposta": ["Comédia", "Romance"],
    "Homem de Ferro": ["Ação", "Ficção Científica"],
    "O Lado Bom da Vida": ["Drama", "Romance"],
    "A Morte te dá Parabéns": ["Terror", "Comédia"],
    "Her": ["Ficção Científica", "Romance"],
    "Jogos Vorazes": ["Ação", "Drama"],
    "Ela é Demais": ["Romance", "Comédia"],
}

# Cálculo da pontuação ponderada
resultados = []
for filme, tags in recomendacoes.items():
    score = sum(pesos_genero[genero] for genero in tags if genero in preferencias)
    if score > 0:
        resultados.append((filme, score))

# Exibição
if preferencias:
    st.subheader("🎬 Recomendações Personalizadas")

    if resultados:
        resultados.sort(key=lambda x: x[1], reverse=True)
        df = pd.DataFrame(resultados, columns=["Filme", "Pontuação"])
        st.table(df)

        fig = px.bar(df, x="Filme", y="Pontuação", title="Pontuação Ponderada dos Filmes")
        st.plotly_chart(fig)
    else:
        st.info("Nenhuma recomendação para os gêneros selecionados.")
else:
    st.warning("Selecione pelo menos um gênero.")
