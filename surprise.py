import streamlit as st
import time
import random

# --- 1. CONFIGURATION & FONCTIONS ---
st.set_page_config(page_title="Libération Janvier", page_icon="❄️", layout="centered")

def get_css():
    """Génère le CSS global et l'effet de neige"""
    return """
    <style>
    /* Fond global */
    .stApp { background-color: #0E1117; }
    
    /* Inputs et Textes */
    .stTextInput > div > div > input { color: white; background-color: #262730; }
    p, label, h1, h2, h3 { color: white !important; }
    
    /* Bouton personnalisé */
    div.stButton > button {
        width: 100%; height: 60px;
        background: linear-gradient(90deg, #FF007F, #6600FF);
        color: white; font-size: 18px; font-weight: bold;
        border: none; border-radius: 12px; transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(102, 0, 255, 0.6);
    }
    
    /* Animation Neige (Background) */
    .snowflake {
        color: #fff; font-size: 1em; font-family: Arial;
        text-shadow: 0 0 1px #000; position: fixed;
        top: -10%; z-index: 9999; user-select: none;
        cursor: default; animation-name: snowflakes-fall, snowflakes-shake;
        animation-duration: 10s, 3s; animation-timing-function: linear, ease-in-out;
        animation-iteration-count: infinite, infinite; animation-play-state: running, running;
    }
    @keyframes snowflakes-fall { 0% { top: -10%; } 100% { top: 100%; } }
    @keyframes snowflakes-shake { 0% { transform: translateX(0px); } 50% { transform: translateX(80px); } 100% { transform: translateX(0px); } }
    .snowflake:nth-of-type(0) { left: 1%; animation-delay: 0s, 0s; }
    .snowflake:nth-of-type(1) { left: 10%; animation-delay: 1s, 1s; }
    .snowflake:nth-of-type(2) { left: 20%; animation-delay: 6s, .5s; }
    .snowflake:nth-of-type(3) { left: 30%; animation-delay: 4s, 2s; }
    .snowflake:nth-of-type(4) { left: 40%; animation-delay: 2s, 2s; }
    .snowflake:nth-of-type(5) { left: 50%; animation-delay: 8s, 3s; }
    .snowflake:nth-of-type(6) { left: 60%; animation-delay: 6s, 2s; }
    .snowflake:nth-of-type(7) { left: 70%; animation-delay: 2.5s, 1s; }
    .snowflake:nth-of-type(8) { left: 80%; animation-delay: 1s, 0s; }
    .snowflake:nth-of-type(9) { left: 90%; animation-delay: 3s, 1.5s; }
    </style>
    
    <div class="snowflake">❅</div><div class="snowflake">❅</div>
    <div class="snowflake">❆</div><div class="snowflake">❄</div>
    <div class="snowflake">❅</div><div class="snowflake">❆</div>
    <div class="snowflake">❄</div><div class="snowflake">❅</div>
    <div class="snowflake">❆</div><div class="snowflake">❄</div>
    """

def create_ticket_html(prenom, batterie, activite, couleur):
    """Génère le HTML du ticket"""
    return f"""
    <div style="font-family: 'Helvetica Neue', sans-serif; border: 4px dashed {couleur}; 
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); 
        padding: 30px; border-radius: 20px; text-align: center; margin-top: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); position: relative; overflow: hidden;">
        
        <div style="background-color: {couleur}; color: #000; font-weight: 800; 
            padding: 5px 15px; display: inline-block; border-radius: 50px; 
            margin-bottom: 15px; text-transform: uppercase; font-size: 12px; letter-spacing: 1px;">
            Session Terminée
        </div>
        
        <h1 style="color: white; margin: 0; font-size: 42px; text-transform: uppercase; 
            letter-spacing: 4px; text-shadow: 0px 0px 10px {couleur}; line-height: 1.1;">
            PASS LIBERTÉ
        </h1>
        
        <p style="color: #aaa; font-size: 14px; margin-top: 5px; font-style: italic;">
            Délivré aux survivants de Janvier
        </p>
        
        <h2 style="color: white; font-size: 45px; margin: 15px 0; font-weight: 900;">{prenom}</h2>
        
        <div style="border-top: 2px solid #444; margin: 25px 0; width: 80%; margin-left: 10%;"></div>
        
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px;">
            <div style="text-align: left;">
                <p style="color: {couleur}; font-size: 11px; text-transform: uppercase; margin: 0; letter-spacing: 1px;">Batterie</p>
                <p style="color: white; font-size: 22px; font-weight: bold; margin: 5px 0;">{batterie}</p>
            </div>
            <div style="font-size: 35px; animation: float 3s ease-in-out infinite;">✈️</div>
            <div style="text-align: right;">
                <p style="color: {couleur}; font-size: 11px; text-transform: uppercase; margin: 0; letter-spacing: 1px;">Mission</p>
                <p style="color: white; font-size: 22px; font-weight: bold; margin: 5px 0;">{activite}</p>
            </div>
        </div>
        
        <div style="margin-top: 30px; font-size: 11px; color: #666;">
            Code ID: {random.randint(10000, 99999)}-NO-BRAIN<br>
            <i>Ce document autorise une sieste de durée indéterminée.</i>
        </div>
        
        <style>
        @keyframes float {{ 0% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-10px); }} 100% {{ transform: translateY(0px); }} }}
        </style>
    </div>
    """

# --- 2. INITIALISATION ---
st.markdown(get_css(), unsafe_allow_html=True)

# Initialisation du session_state pour garder le ticket affiché
if 'ticket_html' not in st.session_state:
    st.session_state.ticket_html = None

# --- 3. INTERFACE UTILISATEUR ---
st.title("❄️ Check-out : Session Janvier")
st.caption("Formalités de sortie avant la pause bien méritée.")

col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Chloé")
    # Mapping des valeurs du slider pour récupérer juste le % ou le texte
    niveau_batterie = st.select_slider("Niveau de batterie actuel :", 
                                options=["0% (HS)", "20% (Éco)", "50% (Ça va)", "100% (Machine)"],
                                value="20% (Éco)")

with col2:
    activite = st.selectbox("Objectif prioritaire :", 
                         ["Hibernation 🐻", "Raclette Party 🧀", "Binge Watching 📺", "Ski intensif ⛷️", "Plage (Rêve) 🏖️"])
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")

st.markdown("---")

# --- 4. LOGIQUE DU BOUTON ---
if st.button("ACTIVER LE MODE VACANCES 🚀"):
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # Messages de chargement aléatoires
        loading_msgs = [
            "Suppression des réveils...",
            "Archivage des soucis...",
            "Calcul de la quantité de fromage nécessaire...",
            "Déconnexion du cerveau..."
        ]
        
        barre = st.progress(0, text="Initialisation...")
        for i in range(100):
            time.sleep(0.015)
            # Change le texte tous les 25%
            if i % 25 == 0:
                msg = loading_msgs[int(i/25)]
                barre.progress(i + 1, text=msg)
            else:
                barre.progress(i + 1)
        
        time.sleep(0.2)
        barre.empty()
        st.balloons()
        
        # Génération et stockage du ticket dans la session
        st.session_state.ticket_html = create_ticket_html(prenom, niveau_batterie, activite, couleur_choisie)

# --- 5. AFFICHAGE DU RÉSULTAT ---
if st.session_state.ticket_html:
    st.markdown(st.session_state.ticket_html, unsafe_allow_html=True)
    
    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger mon Pass (HTML)",
        data=st.session_state.ticket_html,
        file_name=f"pass_liberte_{prenom}.html",
        mime="text/html"
    )
    
    if st.button("🔄 Recommencer"):
        st.session_state.ticket_html = None
        st.rerun()
