import streamlit as st
import time
import base64
import random

# --- 1. FONCTIONS TECHNIQUES ---
@st.cache_data
def get_audio_base64(fichier_audio):
    try:
        with open(fichier_audio, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def jouer_musique_secure(fichier_audio):
    b64 = get_audio_base64(fichier_audio)
    if b64:
        md = f"""<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
        st.markdown(md, unsafe_allow_html=True)
    else:
        st.toast("⚠️ Note : Layla.mp3 est absent, mais on continue en silence !", icon="🔇")

# --- 2. STYLE & DESIGN ---
if 'neige_html' not in st.session_state:
    flocons_types = ['❄', '❅', '❆']
    divs_flocons = ""
    for i in range(100): 
        left = random.uniform(0, 100)
        size = random.randint(10, 35)
        duration = random.uniform(5, 15)
        delay = random.uniform(0, 10)
        opacity = random.uniform(0.2, 0.9)
        char = random.choice(flocons_types)
        blur = "2px" if size > 25 else "0px"
        divs_flocons += f'<div class="snowflake" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s; animation-delay:{delay}s; opacity:{opacity}; filter:blur({blur});">{char}</div>'
    st.session_state.neige_html = divs_flocons

# ATTENTION : Toutes les accolades CSS sont doublées {{ }} ici
st.markdown(f"""
<style>
.stApp {{
    background-color: #0E1117;
}}

h1, h2, h3, p, label, .stMarkdown {{
    color: white !important;
}}

.snowflake {{
    color: #ffffff;
    position: fixed;
    top: -10%;
    z-index: 9999;
    user-select: none;
    pointer-events: none;
    animation-name: fall, shake;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
}}

.diag-card {{
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    border-left: 5px solid;
    background-color: rgba(255, 255, 255, 0.05);
    animation: fadeIn 0.4s ease-out;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(5px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fall {{
    0% {{ top: -10%; }}
    100% {{ top: 110%; }}
}}

@keyframes shake {{
    0%, 100% {{ transform: translateX(0) rotate(0deg); }}
    50% {{ transform: translateX(30px) rotate(20deg); }}
}}

.stButton>button {{
    width: 100%;
    height: 70px;
    background: linear-gradient(90deg, #FF007F, #6600FF);
    color: white !important;
    font-size: 22px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
}}
</style>
{st.session_state.neige_html}
""", unsafe_allow_html=True)

# --- 3. INTERFACE UTILISATEUR ---
st.title("❄️ Presque la quille !")
st.subheader("Check Out : Session Janvier")

prenom = st.text_input("C'est pour quel nom le ticket ?", placeholder="Ton petit nom ici...")
if prenom:
    st.write(f"Parfait **{prenom}**, on s'occupe de ton exfiltration ✨")

st.divider()

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.write("**🪫 Ton niveau d'énergie**")
    batterie = st.select_slider(
        "Alors, comment tu te sens ?", 
        options=["💀 HS", "😫 Fatigué", "😐 Ça va", "😁 En forme", "🚀 Prêt à tout"],
        value="😫 Fatigué"
    )
    
    diags = {
        "💀 HS": {"t": "Alerte : Zombie détecté", "p": "Diagnostic : Mort clinique. Réanimation par perfusion de sieste conseillée", "c": "error"},
        "😫 Fatigué": {"t": "Mode Éco activé", "p": "Ordonnance : 3 jours de pyjama et interdiction de regarder les mails", "c": "warning"},
        "😐 Ça va": {"t": "Survivant stable", "p": "Mouais, on y croit 🤨 blablablablabla pour la 2e ligne", "c": "info"},
        "😁 En forme": {"t": "Anomalie suspecte", "p": "Trop d'énergie pour un mois de Janvier. On surveille ça de près...", "c": "success"},
        "🚀 Prêt à tout": {"t": "Veuillez redescendre", "p": "Il faut trouver un truc, je sais pas quoi, blablablabla", "c": "success2"}
    }
    
    info = diags[batterie]
    couleurs_douces = {"error": "#FF4B4B", "warning": "#FFA421", "info": "#00C0F2", "success": "#00D488", "success2": "#00d42e"}
    color = couleurs_douces.get(info['c'], "#FFFFFF")

    st.markdown(f"""
        <div class="diag-card" style="border-color: {color};">
            <p style="color: {color} !important; font-weight: bold; margin-bottom: 5px;">{info['t']}</p>
            <p style="color: white !important; margin: 0;">{info['p']}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.write("**🌴 Ton projet secret**")
    activite = st.selectbox(
        "Ta priorité absolue ?", 
        ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon De Films 📺", "Aller skier ⛷️", "Fuite à l'étranger ✈️", "Apéro infini 🍻"]
    )
    transport = st.selectbox(
        "Tu t'en vas comment ?", 
        ["Téléportation", "À la nage", "Dos de Dragon", "Trottinette Électrique", "Tapis Volant", "Uber Copter"]
    )

st.write("---")
_, bt_center, _ = st.columns([1, 2, 1])
with bt_center:
    bouton_clique = st.button("IMPRIMER LE BOARDING PASS 🚀")

# --- 4. LOGIQUE D'ACTIVATION ---
if bouton_clique:
    if not prenom:
        st.warning("⚠️ Donne-moi ton prénom d'abord !")
    else:
        jouer_musique_secure("Layla.mp3") 
        barre = st.progress(0, text="Calcul de la trajectoire vers la liberté...")
        for i in range(100):
            time.sleep(0.01) 
            barre.progress(i + 1)
        barre.empty()
        st.balloons()
        st.hearts()
        
        couleur_choisie = "#00FFFF"
        html_ticket = f"""
        <div style="font-family: Arial; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 0 25px {couleur_choisie}50; animation: slideUp 0.8s ease-out;">
            <div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">Session Janvier Terminée</div>
            <h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px {couleur_choisie};">PASS LIBERTÉ</h1>
            <p style="color: #cccccc; font-style: italic;">Valable exclusivement pour :</p>
            <h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
            <div style="border-top: 1px solid #555; margin: 20px 0;"></div>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 10px;">
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">ÉNERGIE</p><p style="color: white; font-weight: bold;">{batterie}</p></div>
                <div style="font-size: 25px;">✈️</div>
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">DESTINATION</p><p style="color: white; font-weight: bold;">{activite}</p></div>
                <div style="font-size: 25px;">🚀</div>
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">TRANSPORT</p><p style="color: white; font-weight: bold;">{transport}</p></div>
            </div>
            <div style="margin-top: 30px; font-size: 12px; color: #777;">Ce document certifie que le cerveau de l'utilisateur est officiellement en veille (désolé)<br>Validité : Jusqu'à la reprise</div>
        </div>
        <style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
