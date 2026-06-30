import streamlit as st
import google.generativeai as genai

# 1. Configuration (Remplace 'TA_CLE_API_ICI' par la tienne obtenue sur Google AI Studio)
# Pour une sécurité maximale sur Streamlit Cloud, on utilisera les Secrets plus tard.
genai.configure(api_key="TA_CLE_API_ICI")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Gépoké", page_icon="🎮")
st.title("🎮 Gépoké à votre service !")
st.subheader("Qu'est-ce qu'il y a à savoir aujourd'hui sur les Pokémon ?")

# 2. Sélecteur de langue
LANGUAGES = ["English", "Français", "Español", "Deutsch", "简体中文", "Português", "Русский", "Indonesia", "日本語"]
lang = st.sidebar.selectbox("Language / Langue", LANGUAGES)

# 3. Initialisation de l'archive
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Logique de l'IA
if prompt := st.chat_input("Pose ta question sur les Pokémon..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Gépoké cherche dans le Pokédex..."):
            try:
                instruction = f"Tu es Gépoké, une IA experte en Pokémon. Réponds à la question suivante en {lang} : {prompt}. Si la question ne concerne pas Pokémon, refuse poliment."
                response = model.generate_content(instruction)
                reponse_texte = response.text
                st.markdown(reponse_texte)
                st.session_state.messages.append({"role": "assistant", "content": reponse_texte})
            except Exception as e:
                st.error("Erreur de connexion avec l'IA. Vérifie ta clé API.")
