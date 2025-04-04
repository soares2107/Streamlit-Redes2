import streamlit as st
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
from collections import Counter
import re
import io


st.title("📝 Análise de Texto em Tempo Real")

# Entrada de texto
texto = st.text_area("Digite ou cole seu texto aqui:")

if texto:
    # Limpeza simples do texto
    palavras = re.findall(r'\b\w+\b', texto.lower())

    # Contagem de palavras e caracteres
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    st.subheader("📊 Estatísticas")
    st.write(f"**Palavras:** {num_palavras}")
    st.write(f"**Caracteres:** {num_caracteres}")

  # Nuvem de palavras
    st.subheader("☁️ Nuvem de Palavras")
    wc = WordCloud(width=800, height=300, background_color='white').generate(" ".join(palavras))

    # Salvar a imagem da nuvem num buffer como imagem PIL
    img_buffer = io.BytesIO()
    wc.to_image().save(img_buffer, format='PNG')
    img_buffer.seek(0)

    st.image(img_buffer)

    # Palavras mais frequentes
    st.subheader("🔝 5 Palavras Mais Frequentes")
    contagem = Counter(palavras)
    top5 = contagem.most_common(5)

    for palavra, freq in top5:
        st.write(f"**{palavra}**: {freq}x")
