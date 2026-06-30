import streamlit as st
import requests

# 1. Dictionnaire des traductions
TRANSLATIONS = {
    "English": {"title": "Gépoké at your service!", "input": "Search a Pokémon...", "not_found": "Pokémon not found!"},
    "Français": {"title": "Gépoké à votre service !", "input": "Chercher un Pokémon...", "not_found": "Pokémon non trouvé !"},
    "Español": {"title": "¡Gépoké a su servicio!", "input": "Busca un Pokémon...", "not_found": "¡Pokémon no encontrado!"},
    "Deutsch": {"title": "Gépoké zu deinen Diensten!", "input": "Suche ein Pokémon...", "not_found": "Pokémon nicht gefunden!"},
    "简体中文": {"title": "Gépoké 为您服务！", "input": "搜索宝可梦...", "not_found": "未找到宝可梦！"},
    "Português": {"title": "Gépoké ao seu dispor!", "input": "Procure um Pokémon...", "not_found": "Pokémon não encontrado!"},
    "عربي": {"title": "جيبوكيه في خدمتك!", "input": "ابحث عن بوكيمون...", "not_found": "لم يتم العثور على البوكيمون!"},
    "Русский": {"title": "Gépoké к вашим услугам!", "input": "Искать покемона...", "not_found": "Покемон не найден!"},
    "Indonesia": {"title": "Gépoké siap melayani!", "input": "Cari Pokémon...", "not_found": "Pokémon tidak ditemukan!"},
    "日本語": {"title": "Gépokéがお手伝いします！", "input": "ポケモンを検索...", "not_found": "ポケモンが見つかりません！"}
}

st.set_page_config(page_title="Gépoké", page_icon="🎮")

# 2. Sélecteur de langue dans la barre latérale
lang = st.sidebar.selectbox("Language / Langue", list(TRANSLATIONS.keys()))
t = TRANSLATIONS[lang] # Variable raccourcie pour les textes

st.title(f"🎮 {t['title']}")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_pokemon_data(name, lang):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"**{name.capitalize()}** : {data['weight']/10} kg."
        else:
            return t['not_found']
    except:
        return "Error"

# Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(t['input']):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        reponse = get_pokemon_data(prompt.strip(), lang)
        st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})
