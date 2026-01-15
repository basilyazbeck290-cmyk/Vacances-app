import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Libération Janvier", page_icon="🥂", layout="centered")

# CSS GLOBAL
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    h1, p, h2, h3 { text-align: center !important; }
    .stTextInput > div > div > input { color: white; background-color: #262730; }
    label, .stSlider p { color: white !important; }
    .stButton>button {
        width: 100%; height: 70px;
        background: linear-gradient(90deg, #FF007F, #6600FF);
        color: white; font-size: 20px; font-weight: bold;
        border: none; border-radius: 35px;
        transition: 0.4s; box-shadow: 0px 5px 15px rgba(0,0,0,0.5);
    }
    .stButton>button:hover { transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ET FORMULAIRE ---
st.title("🥂 Check-out : Session Janvier")
st.write("Formalités de sortie avant la pause bien méritée.")

col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Chloé")
    # SLIDER LINEAIRE CORRIGÉ
    batterie_valeur = st.slider("Niveau de batterie (%) :", 0, 100, 20)
    
    # Logique du texte de batterie
    if batterie_valeur < 10: batterie_texte = f"{batterie_valeur}% (Survie 🆘)"
    elif batterie_valeur < 30: batterie_texte = f"{batterie_valeur}% (Mode Éco 🪫)"
    elif batterie_valeur < 70: batterie_texte = f"{batterie_valeur}% (Ça tient)"
    else: batterie_texte = f"{batterie_valeur}% (Machine 🤖)"

with col2:
    activite = st.selectbox("Objectif :", 
         ["Hibernation 🐻", "Raclette 🧀", "Séries 📺", "Ski ⛷️", "Apéro 🍹"])
    couleur_choisie = st.color_picker("Couleur Pass :", "#00FFFF")

st.write("")

# --- 3. BOUTON CENTRÉ ---
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if st.button("ACTIVER LE MODE VACANCES 🚀"):
        if not prenom:
            st.warning("⚠️ Il faut ton prénom !")
        else:
            with st.spinner("Création du Pass..."):
                time.sleep(1)
            
            st.balloons()
            st.toast(f"Libération confirmée pour {prenom} !", icon="🎉")

            # --- 4. LE CODE HTML (COLLÉ À GAUCHE = TRES IMPORTANT) ---
            # Ne rajoute pas d'espace au début des lignes ci-dessous !
            html_ticket = f"""
<div style="font-family: Arial, sans-serif; border: 2px solid {couleur_choisie}; background: linear-gradient(135deg, #121212 0%, #2a2a2a 100%); border-radius: 20px; margin-top: 20px; box-shadow: 0 0 30px {couleur_choisie}40; color: white; max-width: 500px; margin-left: auto; margin-right: auto; overflow: hidden; animation: slideUp 0.8s ease-out;">
    <div style="background: {couleur_choisie}; padding: 15px; text-align: center;">
        <h3 style="margin: 0; color: black; font-weight: 900; letter-spacing: 2px;">BOARDING PASS</h3>
    </div>
    <div style="padding: 25px;">
        <div style="display: flex; justify-content: space-between;">
            <div style="text-align: left;">
                <p style="color: #888; font-size: 10px; text-transform: uppercase; margin: 0; text-align: left !important;">Passager</p>
                <h2 style="margin: 0; font-size: 28px; text-shadow: 0 0 10px {couleur_choisie}; text-align: left !important;">{prenom}</h2>
            </div>
            <div style="text-align: right;">
                <p style="color: #888; font-size: 10px; text-transform: uppercase; margin: 0; text-align: right !important;">Date</p>
                <h4 style="margin: 0; font-size: 18px; text-align: right !important;">JAN 2026</h4>
            </div>
        </div>
        <div style="margin: 15px 0; border-top: 2px dashed #444;"></div>
        <div style="display: flex; justify-content: space-between;">
            <div style="text-align: left;">
                <p style="color: {couleur_choisie}; font-size: 10px; margin: 0; text-align: left !important;">BATTERIE</p>
                <p style="font-size: 16px; font-weight: bold; margin: 0; text-align: left !important;">{batterie_texte}</p>
            </div>
            <div style="text-align: right;">
                <p style="color: {couleur_choisie}; font-size: 10px; margin: 0; text-align: right !important;">DESTINATION</p>
                <p style="font-size: 16px; font-weight: bold; margin: 0; text-align: right !important;">{activite}</p>
            </div>
        </div>
        <div style="margin-top: 20px; background: white; padding: 10px; border-radius: 10px; display: flex; align-items: center;">
            <svg width="50" height="50" viewBox="0 0 100 100"><path d="M0 0h100v100H0z" fill="white"/><path d="M10 10h30v30h-30z M60 10h30v30h-30z M10 60h30v30h-30z M50 50h10v10h-10z M20 20h10v10h-10z" fill="black"/></svg>
            <div style="color: black; margin-left: 15px; flex-grow: 1;">
                <p style="font-size: 10px; margin: 0; color: black !important; text-align: right !important;">ACCESS GRANTED</p>
                <p style="font-size: 14px; font-weight: bold; margin: 0; color: black !important; text-align: right !important;">LIBRE ✅</p>
            </div>
        </div>
    </div>
</div>
<style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
"""
            st.markdown(html_ticket, unsafe_allow_html=True)
