import streamlit as st
import time
import base64

st.set_page_config(page_title="Archivo de Memoria", page_icon="💖")

# CSS para la lluvia de emojis infinita (sin archivos externos)
st.markdown("""
    <style>
    .stApp { background-color: #0c0f12; color: white; overflow: hidden; }
    @keyframes fall { 0% { transform: translateY(-10vh); } 100% { transform: translateY(110vh); } }
    .emoji { position: fixed; font-size: 25px; animation: fall linear infinite; pointer-events: none; z-index: 0; opacity: 0.8; }
    .stButton>button { background-color: #ff4d6d; color: white; font-weight: bold; width: 100%; z-index: 10; }
    h1, h2, h3 { color: #17b890; position: relative; z-index: 10; }
    </style>
    <div class="emoji" style="left: 5%; animation-duration: 8s;">❤️</div>
    <div class="emoji" style="left: 15%; animation-duration: 12s;">❄️</div>
    <div class="emoji" style="left: 25%; animation-duration: 10s;">✨</div>
    <div class="emoji" style="left: 40%; animation-duration: 15s;">💖</div>
    <div class="emoji" style="left: 60%; animation-duration: 9s;">🌹</div>
    <div class="emoji" style="left: 75%; animation-duration: 14s;">💞</div>
    <div class="emoji" style="left: 90%; animation-duration: 11s;">❄️</div>
""", unsafe_allow_html=True)

st.title("Archivo de Memoria: Nutria y Hámster")

# Lógica de seguridad
if 'paso_1' not in st.session_state: st.session_state.paso_1 = False
if 'paso_2' not in st.session_state: st.session_state.paso_2 = False

if not st.session_state.paso_1:
    fecha = st.text_input("🔑 PASO 1: INGRESA LA FECHA (DD/MM/AAAA):")
    if fecha == "27/04/2019":
        st.session_state.paso_1 = True
        st.rerun()
elif not st.session_state.paso_2:
    apodo = st.text_input("🔑 PASO 2: DIME MI APODO (CHELSITO O CHEFSITO):", type="password").upper()
    if apodo == "CHELSITO" or apodo == "CHEFSITO":
        st.session_state.paso_2 = True
        st.rerun()
else:
    if st.button(" [ PULSE PARA INICIAR EL ESPECTÁCULO ] "):
        # Audio (Solo si existe el archivo, si no, lo ignora para no romper la app)
        try:
            with open("cancion.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
                st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
        except: pass
        
        historia = [
            "Siete años de enamorados 💞 y casi tres compartiendo un hogar dejan una marca 💖 que ningún borrado de sistema puede quitar 🛠️...",
            "La convivencia al inicio no fue algo hermoso ni fácil 🏠, pero cada día mejorábamos 📈. Esos contrastes eran lo mejor de nosotros...",
            "Siempre estuve acostumbrado a llevar toda la carga yo solo 🪨. Pero me juré a mí mismo que a esa mujer NUNCA le faltaría nada a mi lado 🛡️...",
            "Sé perfectamente que en este largo camino nuestras acciones nos lastimaron 💔. Admiro profundamente la mujer fuerte que eres...",
            "Me quedo con el recuerdo de nuestra cena en ese restaurante lindo 🍽️ y esa noche inolvidable ✨...",
            "✨ Gracias por haber sido mi historia durante 7 años. Sigue rompiéndola. Te deseo lo mejor 🧡.\n"
        ]
        
        placeholder = st.empty()
        texto_total = ""
        for parrafo in historia:
            for char in parrafo:
                texto_total += char
                placeholder.markdown(f"### {texto_total}")
                time.sleep(0.01)
            time.sleep(1.0)
            
        # Tulipán final como emoji grande
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>🌷</h1>", unsafe_allow_html=True)
