import streamlit as st
import time
import base64

st.set_page_config(page_title="Archivo de Memoria", page_icon="💖")

# CSS para la lluvia de emojis infinita y el diseño limpio
st.markdown("""
    <style>
    .stApp { background-color: #0c0f12; color: white; overflow: hidden; }
    @keyframes fall { 
        0% { transform: translateY(-10vh); } 
        100% { transform: translateY(110vh); } 
    }
    .emoji { 
        position: fixed; font-size: 25px; animation: fall linear infinite; 
        pointer-events: none; z-index: 0; opacity: 0.8;
    }
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

# Estados para la lógica paso a paso
if 'paso_1' not in st.session_state: st.session_state.paso_1 = False
if 'paso_2' not in st.session_state: st.session_state.paso_2 = False

if not st.session_state.paso_1:
    fecha = st.text_input("🔑 PASO 1: INGRESA LA FECHA QUE INICIÓ TODO (DD/MM/AAAA):")
    if fecha == "27/04/2019":
        st.session_state.paso_1 = True
        st.rerun()
    elif fecha != "":
        st.error("❌ Fecha incorrecta.")

elif not st.session_state.paso_2:
    st.success("¡Fecha correcta! Ahora el último paso.")
    apodo = st.text_input("🔑 PASO 2: DIME MI APODO RECIENTE EN MAYUSCULAS :", type="password").upper()
    if apodo == "CHELSITO" or apodo == "CHEFSITO" or apodo == "CHESITO":
        st.session_state.paso_2 = True
        st.rerun()
    elif apodo != "":
        st.error("❌ Apodo incorrecto.")

else:
    st.success("¡Acceso total concedido!")
    if st.button(" [ PULSE PARA INICIAR EL ESPECTÁCULO ] "):
        # Reproducción de audio
        with open("cancion.mp3", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
        
        historia = [
            "Siete años de enamorados 💞 y casi tres compartiendo un hogar dejan una marca 💖 que ningún borrado de sistema puede quitar 🛠️. Hemos pasado por absolutamente de todo, desde momentos llenos de adrenalina como el canotaje en Tarapoto 🚣 donde la pasamos de la ctmr, hasta la inmensa alegría de poder cumplirte cada capricho, obsequiándote esos perfumes 💐 o los iPhones 📱 que veías. Poder darte todo eso sabiendo que antes no teníamos cómo, ha sido de las satisfacciones más hermosas y puras ✨ que me llevo en el corazón ❤️.\n\n",
            "La convivencia al inicio no fue algo hermoso ni fácil 🏠, pero cada día mejorábamos 📈. Me acuerdo y me río solo de cuando cocinaste esa sopa 🍲 y le echaste un huevo que terminó estando podrido 🥚; se echó a perder todo, pero nos reímos demasiado 😂. Esos contrastes eran lo mejor de nosotros. Por eso, lo que más voy a extrañar con el alma entera son esas amanecidas que nos dábamos casi todos los días 🌜: conversar en la madrugada, hablar de nuestro futuro 🗺️, de nuestros problemas, de nuestras dudas... de todo hablábamos 🗣️. Pasamos también llantos profundos, como cuando se nos extravió nuestro gatito en ese taxi 🐱💔 y que me deprimió tanto 🥺; pero ahí estuvimos, apoyándonos y conviviendo.\n\n",
            "Siempre estuve acostumbrado a llevar toda la carga yo solo 🪨. Hubo una noche en que mi método para generar dinero se vino abajo 📉; mientras dormías, lloré de confusión pidiéndole ayuda a Dios 🙏 y me juré a mí mismo que a esa mujer NUNCA le faltaría nada a mi lado 🛡️. Me senté a buscar soluciones y las hallé, desordenando mi vida entera para que tú estuvieras segura. Por eso, cuando te levantabas llorando de tus sueños 😢, lo único que me importaba era abrazarte muy fuerte 🫂, besarte la frente 😘 y decirte al oído: 'Tranquila, nadie te podrá lastimar'. Quise ser tu refugio 🔐.\n\n",
            "Sé perfectamente que en este largo camino nuestras acciones nos lastimaron 💔, y hoy tengo la entera madurez de reconocer que fui yo quien cometió el error ⚖️ que terminó afectando lo nuestro. No busco excusas 🗳️. Admiro profundamente la mujer fuerte que eres; toda esa carga pesada de tu infancia 🎒 la estás transformando en superación al estudiar Psicología 🧠. Fuiste hecha para sanar e iluminar 🌟 la vida de otros, y sé que vas a ser una profesional extraordinaria 🎓. Nunca olvides de lo que eres capaz.\n\n",
            "Me quedo con el recuerdo de nuestra cena en ese restaurante lindo 🍽️, con tus flores 🌹 y esa noche inolvidable ✨ donde todo el esfuerzo valió la pena. Éxitos en tu universidad y en cada paso que des 👣.\n\n",
            "✨ Gracias por haber sido mi historia durante 7 años. Sigue rompiéndola. Te deseo lo mejor 🧡.\n"
        ]
        
        placeholder = st.empty()
        texto_total = ""
        for parrafo in historia:
            for char in parrafo:
                texto_total += char
                placeholder.markdown(f"### {texto_total}")
                time.sleep(0.08)
            time.sleep(2.0)
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>🌷</h1>", unsafe_allow_html=True)
