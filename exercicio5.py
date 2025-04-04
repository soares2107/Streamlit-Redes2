import streamlit as st

st.title("📋 Formulário com Validação")

# Inicializar estado se não existir
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "reset" not in st.session_state:
    st.session_state.reset = False

# Botão para limpar o formulário
if st.button("🧹 Limpar Formulário"):
    st.session_state.submitted = False
    st.session_state.reset = True

# Formulário
with st.form("formulario_usuario"):
    nome = st.text_input("Nome:", value="" if st.session_state.reset else "")
    idade = st.number_input("Idade:", min_value=0, max_value=120, step=1, value=0 if st.session_state.reset else 25)
    cores = st.multiselect("Preferência de cor:", ["Azul", "Verde", "Vermelho", "Amarelo", "Preto", "Branco"],
                           default=[] if st.session_state.reset else None)
    
    submitted = st.form_submit_button("Enviar")

    if submitted:
        st.session_state.submitted = True
        st.session_state.reset = False

# Mensagem personalizada
if st.session_state.submitted:
    if nome and 0 <= idade <= 120:
        cores_formatadas = ", ".join(cores) if cores else "nenhuma cor"
        st.success(f"Olá, {nome}, com {idade} anos, você gosta de {cores_formatadas}!")
    else:
        st.error("Por favor, insira um nome válido e uma idade entre 0 e 120.")
