import streamlit as st
import time
import base64
import random

# --- 1. FONCTIONS TECHNIQUES ---
@st.cache_data
def get_audio_base64(fichier_audio):
    """Encode l'audio pour éviter les rechargements inutiles."""
    try:
        with open(fichier_audio, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def jouer_musique_secure(fichier_audio):
    """Lance la musique sans faire planter l'app si le fichier manque."""
    b64 = get_audio_base64(fichier_audio)
    if b64:
        md = f"""<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
        st.markdown(md, unsafe_allow_html=True)
    else:
        st.toast("⚠️ Note : Layla.mp3 est absent, mais on continue en silence !", icon="🔇")

# --- 2. STYLE & DESIGN CUSTOM ---
st.set_page_config(page_title="Mission : Libération", page_icon="❄️", layout="centered")


flocons_html = ""
for i in range(15):
    left = random.randint(0, 100)
    size = random.randint(12, 28)
    duration = random.randint(8, 18)
    delay = random.randint(0, 10)

    flocons_html += f"""
    <div class="snowflake"
         style="
            left:{left}%;
            font-size:{size}px;
            animation-duration:{duration}s;
            animation-delay:{delay}s;">
        ❄
    </div>
    """


st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    p, label, h1, h2, h3 { color: white !important; }
    
    /* Inputs plus doux */
    .stTextInput > div > div > input { border-radius: 10px; background-color: #262730; color: white; }
    div[data-baseweb="select"] > div { border-radius: 10px; background-color: #262730; }

    /* BOUTON ULTRA-STYLÉ */
    .stButton>button {
        width: 100%;
        height: 70px;
        background: linear-gradient(90deg, #FF007F, #6600FF);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
        border-radius: 15px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 25px rgba(102, 0, 255, 0.6);
    }

    
    <style>
    
    /* ANIMATION NEIGE AMÉLIORÉE */
    .snowflake {{
        color: white;
        position: fixed;
        top: -10%;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation-name: fall, shake;
        animation-timing-function: linear, ease-in-out;
        animation-iteration-count: infinite, infinite;
    }}
    
    @keyframes fall {{
        to {{ top: 110%; }}
    }}
    
    @keyframes shake {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(60px); }}
    }}
    
    </style>
    
    {flocons_html}
    """, unsafe_allow_html=True)


# --- 3. INTERFACE UTILISATEUR (La partie "Humaine") ---

st.title("❄️ Presque la quille !")
st.subheader("Check Out : Session Janvier")

with st.container():
    st.write("  ")
    
    # Prénom : Le point de départ
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
        
        # --- LE DIAGNOSTIC (Comble le trou sous le slider) ---
        diags = {
            "💀 HS": {"t": "Alerte : Zombie détecté", "p": "Diagnostic : Mort clinique.\n\nRéanimation par perfusion de sieste conseillée.", "c": "error"},
            "😫 Fatigué": {"t": "Mode Éco activé", "p": "Ordonnance : 3 jours de pyjama et interdiction de regarder les mails.", "c": "warning"},
            "😐 Ça va": {"t": "Survivant stable", "p": "Mouais, on y croit 🤨", "c": "info"},
            "😁 En forme": {"t": "Anomalie suspecte", "p": "Trop d'énergie pour un mois de Janvier.\n\nOn surveille ça de près...", "c": "success"},
            "🚀 Prêt à tout": {"t": "Veuillez redescendre", "p": "Calme-toi sur l'expresso, Elon.\n\nOn est juste en janvier, pas sur Mars.", "c": "success"}
        }
        
        info = diags[batterie]
        st.write(f"**{info['t']}**")
        if info['c'] == "error": st.error(info['p'])
        elif info['c'] == "warning": st.warning(info['p'])
        elif info['c'] == "success": st.success(info['p'])
        else: st.info(info['p'])

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

couleur_choisie = "#00FFFF" # Bleu néon pour le ticket

st.write("---")
bt_left, bt_center, bt_right = st.columns([1, 2, 1])
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
        time.sleep(0.2)
        barre.empty()
        
        st.balloons()
        
        # Le ticket HTML final
        html_ticket = f"""
        <div style="font-family: Arial; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 0 25px {couleur_choisie}50; animation: slideUp 0.8s ease-out;">
            <div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">Session Janvier Terminée</div>
            <h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px 0px {couleur_choisie};">PASS LIBERTÉ</h1>
            <p style="color: #cccccc; font-style: italic;">Valable exclusivement pour :</p>
            <h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
            <div style="border-top: 1px solid #555; margin: 20px 0;"></div>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">ÉNERGIE</p><p style="color: white; font-weight: bold;">{batterie}</p></div>
                <div style="font-size: 25px;">✈️</div>
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">DESTINATION</p><p style="color: white; font-weight: bold;">{activite}</p></div>
                <div style="font-size: 25px;">🚀</div>
                <div><p style="color: {couleur_choisie}; font-size: 12px; margin:0;">TRANSPORT</p><p style="color: white; font-weight: bold;">{transport}</p></div>
            </div>
            <div style="margin-top: 30px; font-size: 12px; color: #777;">Ce document certifie que le cerveau de l'utilisateur est officiellement en veille<br>Validité : Jusqu'à la reprise (désolé)</div>
        </div>
        <style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
