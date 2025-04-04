import streamlit as st
import requests

st.title("🌍 Informações de Países - REST Countries")

pais = st.text_input("Digite o nome de um país em  inglês:", "")

if pais:
    url = f"https://restcountries.com/v3.1/name/{pais}"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()[0]

            nome_oficial = dados['name']['official']
            capital = dados.get('capital', ['Desconhecida'])[0]
            populacao = dados.get('population', 'N/A')
            regiao = dados.get('region', 'N/A')
            idiomas = ", ".join(dados.get('languages', {}).values())
            bandeira = dados['flags']['png']

            st.subheader(f"📋 Informações sobre {nome_oficial}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**População:** {populacao:,}")
            st.write(f"**Região:** {regiao}")
            st.write(f"**Idiomas:** {idiomas}")
            st.image(bandeira, caption="Bandeira")

        else:
            st.error("❌ País não encontrado. Verifique o nome e tente novamente.")

    except Exception as e:
        st.error(f"Erro ao acessar a API: {e}")
