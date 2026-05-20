import streamlit as st
import time
import base64

# Configuración de diseño
st.set_page_config(page_title="Archivo de Memoria", page_icon="💖")
st.markdown("""
    <style>
    .stApp { background-color: #0c0f12; color: white; }
    .stButton>button { background-color: #ff4d6d; color: white; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

st.title("Archivo de Memoria: Nutria y Hámster")

# Función de audio mejorada
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
        st.markdown(md, unsafe_allow_html=True)

if st.button(" [ PULSE PARA INICIAR ] "):
    autoplay_audio("cancion.mp3")
    
    # Texto completo
    historia = [
        "Siete años de enamorados 💞 y casi tres compartiendo un hogar dejan una marca 💖 que ningún borrado de sistema puede quitar 🛠️. Hemos pasado por absolutamente de todo, desde momentos llenos de adrenalina como el canotaje en Tarapoto 🚣 donde la pasamos de la ctmr, hasta la inmensa alegría de poder cumplirte cada capricho, obsequiándote esos perfumes 💐 o los iPhones 📱 que veías. Poder darte todo eso sabiendo que antes no teníamos cómo, ha sido de las satisfacciones más hermosas y puras ✨ que me llevo en el corazón ❤️.\n\n",
        "La convivencia al inicio no fue algo hermoso ni fácil 🏠, pero cada día mejorábamos 📈. Me acuerdo y me río solo de cuando cocinaste esa sopa 🍲 y le echaste un huevo que terminó estando podrido 🥚; se echó a perder todo, pero nos reímos demasiado 😂. Esos contrastes eran lo mejor de nosotros. Por eso, lo que más voy a extrañar con el alma entera son esas amanecidas que nos dábamos casi todos los días 🌜: conversar en la madrugada, hablar de nuestro futuro 🗺️, de nuestros problemas, de nuestras dudas... de todo hablábamos 🗣️. Pasamos también llantos profundos, como cuando se nos extravió nuestro gatito en ese taxi 🐱💔 y que me deprimió tanto 🥺; pero ahí estuvimos, apoyándonos y conviviendo.\n\n",
        "Siempre estuve acostumbrado a llevar toda la carga yo solo 🪨. Hubo una noche en que mi método para generar dinero se vino abajo 📉; mientras dormías, lloré de confusión pidiéndole ayuda a Dios 🙏 y me juré a mí mismo que a esa mujer NUNCA le faltaría nada a mi lado 🛡️. Me senté a buscar soluciones y las hallé, desordenando mi vida entera para que tú estuvieras segura. Por eso, cuando te levantabas llorando de tus sueños 😢, lo único que me importaba era abrazarte muy fuerte 🫂, besarte la frente 😘 y decirte al oído: 'Tranquila, nadie te podrá lastimar'. Quise ser tu refugio 🔐.\n\n",
        "Sé perfectamente que en este largo camino nuestras acciones nos lastimaron 💔, y hoy tengo la entera madurez de reconocer que fui yo quien cometió el error ⚖️ que terminó afectando lo nuestro. No busco excusas 🗳️. Admiro profundamente la mujer fuerte que eres; toda esa carga pesada de tu infancia 🎒 la estás transformando en superación al estudiar Psicología 🧠. Fuiste hecha para sanar e iluminar 🌟 la vida de otros, y sé que vas a ser una profesional extraordinaria 🎓. Nunca olvides de lo que eres capaz.\n\n",
        "Me quedo con el recuerdo de nuestra cena en ese restaurante lindo 🍽️, con tus flores 🌹 y esa noche inolvidable ✨ donde todo el esfuerzo valió la pena. Éxitos en tu universidad y en cada paso que des 👣.\n\n",
        "✨ Gracias por haber sido mi historia durante 7 años. Sigue rompiéndola. Te deseo lo mejor 🧡.\n"
    ]
    
    # Mostrar historia con efecto máquina de escribir
    placeholder = st.empty()
    texto_total = ""
    for parrafo in historia:
        for char in parrafo:
            texto_total += char
            placeholder.markdown(f"### {texto_total}")
            time.sleep(0.02)
            
    st.subheader("👉 Y PARA FINALIZAR UN OBSEQUIO PARA LA NIÑA MAS HERMOSA...")
    st.image("tulipan.png", width=350)
