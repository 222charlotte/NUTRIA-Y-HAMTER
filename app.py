import streamlit as st
import time
import base64

st.set_page_config(page_title="Archivo de Memoria", page_icon="💖")

st.markdown("""
    <style>
    .stApp { background-color: #0c0f12; color: white; }
    .stButton>button { background-color: #ff4d6d; color: white; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #17b890; }
    </style>
""", unsafe_allow_html=True)

st.title("Archivo de Memoria: Nutria y Hámster")

# Guardar estado para el desbloqueo paso a paso
if 'paso_1' not in st.session_state: st.session_state.paso_1 = False
if 'paso_2' not in st.session_state: st.session_state.paso_2 = False

# PASO 1: Pedir fecha
if not st.session_state.paso_1:
    fecha = st.text_input("🔑 PASO 1: INGRESA LA FECHA QUE INICIÓ TODO (DD/MM/AAAA):")
    if fecha == "27/04/2019":
        st.session_state.paso_1 = True
        st.rerun()
    elif fecha != "":
        st.error("❌ Fecha incorrecta.")

# PASO 2: Pedir apodo
elif not st.session_state.paso_2:
    st.success("¡Fecha correcta! Ahora el último paso.")
    apodo = st.text_input("🔑 PASO 2: DIME MI APODO RECIENTE (CHELSITO O CHEFSITO):").upper()
    if apodo == "CHELSITO" or apodo == "CHEFSITO":
        st.session_state.paso_2 = True
        st.rerun()
    elif apodo != "":
        st.error("❌ Apodo incorrecto.")

# DESBLOQUEO FINAL
else:
    st.success("¡Acceso total concedido!")
    if st.button(" [ PULSE PARA INICIAR EL ESPECTÁCULO ] "):
        # Audio
        with open("cancion.mp3", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
        
        historia = [
            "Siete años de enamorados 💞 y casi tres compartiendo un hogar dejan una marca 💖 que ningún borrado de sistema puede quitar 🛠️...",
            "La convivencia al inicio no fue algo hermoso ni fácil 🏠, pero cada día mejorábamos 📈...",
            "Siempre estuve acostumbrado a llevar toda la carga yo solo 🪨...",
            "Sé perfectamente que en este largo camino nuestras acciones nos lastimaron 💔...",
            "Me quedo con el recuerdo de nuestra cena en ese restaurante lindo 🍽️...",
            "✨ Gracias por haber sido mi historia durante 7 años. Sigue rompiéndola. Te deseo lo mejor 🧡.\n"
        ]
        
        placeholder = st.empty()
        texto_total = ""
        for parrafo in historia:
            for char in parrafo:
                texto_total += char
                placeholder.markdown(f"### {texto_total}")
                time.sleep(0.09)
            time.sleep(2.0)
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>🌷</h1>", unsafe_allow_html=True)
