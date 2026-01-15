import streamlit as st
import time
import base64

# --- 1. FONCTIONS ET CACHE (POUR LA VITESSE ⚡) ---

@st.cache_data
def get_audio_base64(fichier_audio):
    """Lit et encode le fichier une seule fois pour le garder en mémoire."""
    with open(fichier_audio, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def jouer_musique_locale(fichier_audio):
    """Joue le son instantanément depuis le cache"""
    b64 = get_audio_base64(fichier_audio)
    md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# --- 2. CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Libération Janvier", page_icon="❄️", layout="centered")

# CSS : Fond sombre, couleurs et... LA NEIGE ❄️
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .stTextInput > div > div > input { color: white; background-color: #262730; }
    p, label { color: white !important; }
    
    /* BOUTON STYLÉ */
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
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 20px rgba(102, 0, 255, 0.5);
    }

    /* NEIGE */
    .snowflake {
        color: #fff; font-size: 1.5em; font-family: Arial; text-shadow: 0 0 1px #000;
        position: fixed; top: -10%; z-index: 9999; user-select: none; pointer-events: none;
        animation: snowflakes-fall 10s linear infinite, snowflakes-shake 3s ease-in-out infinite;
    }
    @keyframes snowflakes-fall { 0% { top: -10%; } 100% { top: 100%; } }
    @keyframes snowflakes-shake { 0% { transform: translateX(0px); } 50% { transform: translateX(80px); } 100% { transform: translateX(0px); } }
    
    .snowflake:nth-of-type(1) { left: 1%; animation-delay: 0s, 0s; }
    .snowflake:nth-of-type(2) { left: 10%; animation-delay: 1s, 1s; }
    .snowflake:nth-of-type(3) { left: 20%; animation-delay: 6s, .5s; }
    .snowflake:nth-of-type(4) { left: 30%; animation-delay: 4s, 2s; }
    .snowflake:nth-of-type(5) { left: 40%; animation-delay: 2s, 2s; }
    .snowflake:nth-of-type(6) { left: 50%; animation-delay: 8s, 3s; }
    .snowflake:nth-of-type(7) { left: 60%; animation-delay: 6s, 2s; }
    .snowflake:nth-of-type(8) { left: 70%; animation-delay: 2.5s, 1s; }
    .snowflake:nth-of-type(9) { left: 80%; animation-delay: 1s, 0s; }
    .snowflake:nth-of-type(10) { left: 90%; animation-delay: 3s, 1.5s; }
    </style>

    <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div>
    <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div>
    <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
""", unsafe_allow_html=True)


# --- 3. INTERFACE ---
st.title("❄️ Check-out : Session Janvier")

col1, col2 = st.columns(2)

with col1:
    st.write("Configure ton extraction vers la liberté.")
    prenom = st.text_input("Ton Prénom (Agent en fuite) :", placeholder="Basil")
    batterie = st.select_slider("État vital actuel :", 
        options=["1% (Critique 💀)", "20% (Eco 😫)", "40% (Fragile 🫤)", "60% (Stable 😐)", "80% (En forme 😁)", "100% (Machine 🚀)"],
        value="20% (Eco 😫)")

with col2:
    st.write("❄️")
    activite = st.selectbox("Mission Prioritaire :", ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon De Films 📺", "Aller skier ⛷️", "Fuite à l'étranger ✈️", "Apéro infini 🍻"])
    # NOUVELLE OPTION AJOUTÉE ICI
    transport = st.selectbox("Moyen d'exfiltration :", ["Téléportation", "Jet Privé", "Dos de Dragon", "Trottinette Électrique", "Tapis Volant", "Uber Copter"])

st.write(""); st.write("")

# SECTION COULEUR CENTRÉE (Pour remplacer les objets interdits)
c_left, c_center, c_right = st.columns([1, 1, 1])
with c_center:
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")

st.write(""); st.write("")

# BOUTON D'ACTION
bt_left, bt_center, bt_right = st.columns([1, 2, 1])
with bt_center:
    bouton_clique = st.button("IMPRIMER LE BOARDING PASS 🚀")


# --- 4. LOGIQUE D'ACTIVATION ---
if bouton_clique:
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # --- A. MUSIQUE (PRIORITÉ ABSOLUE) ---
        try:
            jouer_musique_locale("Layla.mp3") 
        except FileNotFoundError:
            st.error("⚠️ Fichier Layla.mp3 introuvable (Vérifie majuscules/minuscules sur GitHub)")

        # --- B. ANIMATION ---
        barre = st.progress(0, text="Connexion au paradis...")
        for i in range(100):
            time.sleep(0.01) 
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        
        # --- C. BALLONS & TICKET ---
        st.balloons()
        
        html_ticket = f"""
        <div style="font-family: Arial, sans-serif; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; margin-top: 10px; box-shadow: 0 0 25px {couleur_choisie}50; position: relative; overflow: hidden; animation: slideUp 0.8s ease-out;">
            <div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">Session Janvier Terminée</div>
            <h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px 0px {couleur_choisie};">PASS LIBERTÉ</h1>
            <p style="color: #cccccc; font-size: 16px; margin-top: 5px; font-style: italic;">Valable exclusivement pour :</p>
            <h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
            
            <div style="border-top: 1px solid #555; margin: 20px 0;"></div>
            
            <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Batterie</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{batterie.split(' ')[0]}</p></div>
                <div style="font-size: 25px; padding: 0 10px;">✈️</div>
                <div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Destination</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{activite}</p></div>
                <div style="font-size: 25px; padding: 0 10px;">🚀</div>
                <div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Transport</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{transport}</p></div>
            </div>
            
            <div style="margin-top: 30px; font-size: 12px; color: #777;">Ce document certifie que le cerveau de l'utilisateur est officiellement en veille.<br>Validité : Jusqu'à la reprise (désolé).</div>
        </div>
        <style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
