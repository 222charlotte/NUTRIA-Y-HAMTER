import streamlit as st
import time
import base64

# Configuración de la página
st.set_page_config(page_title="Archivo de Memoria", page_icon="💖")

# Estilo para fondo oscuro y diseño estilo terminal
st.markdown("""
    <style>
    .stApp { background-color: #0c0f12; color: white; }
    .stButton>button { background-color: #ff4d6d; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("Archivo de Memoria: Nutria y Hamster")

# Función para reproducir música (codificada en base64 para que la web la lea)
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
        st.markdown(md, unsafe_allow_html=True)

# Lógica del botón
if st.button(" [ PULSE PARA INICIAR ] "):
    autoplay_audio("cancion.mp3")
    
    # El texto de la historia
    historia = "Siete años de enamorados 💞... (aquí pegas todo el texto largo de la carta)..."
    
    # Efecto máquina de escribir en la web
    placeholder = st.empty()
    texto_actual = ""
    for char in historia:
        texto_actual += char
        placeholder.markdown(f"### {texto_actual}")
        time.sleep(0.02)
        
    st.image("tulipan.png", caption="Para la niña más hermosa", width=300)

st.write("✨")