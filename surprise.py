import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Libération Janvier", page_icon="❄️", layout="centered")

# CSS : Fond sombre et forçage des couleurs
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .stTextInput > div > div > input {
        color: white;
        background-color: #262730;
    }
    p, label {
        color: white !important;
    }
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
        margin-top: 20px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 20px rgba(102, 0, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. LE FORMULAIRE ---
st.title("❄️ Check-out : Session Janvier")
st.write("Formalités de sortie avant la pause bien méritée.")

col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Chloé")
    batterie = st.select_slider("Niveau de batterie actuel :", 
                                options=["0% (HS)", "20% (Éco)", "50% (Ça va)", "100% (Machine)"],
                                value="20% (Éco)")

with col2:
    activite = st.selectbox("Objectif prioritaire :", 
                             ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon Séries 📺", "Aller skier ⛷️"])
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")

st.write("")

# --- 3. LE BOUTON ---
if st.button("ACTIVER LE MODE VACANCES 🚀"):
    
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # Petite animation
        barre = st.progress(0, text="Sauvegarde des neurones restants...")
        for i in range(100):
            time.sleep(0.01)
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        
        st.balloons()
        
        # --- 4. LE TICKET (CORRECTION ICI) ---
        # J'ai tout collé à gauche pour éviter que ça s'affiche comme du code
        html_ticket = f"""
<div style="font-family: Arial, sans-serif; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; margin-top: 30px; box-shadow: 0 0 25px {couleur_choisie}50; position: relative; overflow: hidden; animation: slideUp 0.8s ease-out;">
    <div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">
        Session Janvier Terminée
    </div>
    <h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px 0px {couleur_choisie};">
        PASS LIBERTÉ
    </h1>
    <p style="color: #cccccc; font-size: 16px; margin-top: 5px; font-style: italic;">Valable exclusivement pour :</p>
    <h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
    <div style="border-top: 1px solid #555; margin: 20px 0;"></div>
    <div style="display: flex; justify-content: space-around; align-items: center;">
        <div>
            <p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">État des lieux</p>
            <p style="color: white; font-size: 20px; font-weight: bold; margin: 5px 0;">{batterie}</p>
        </div>
        <div style="font-size: 30px;">✈️</div>
        <div>
            <p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Destination</p>
            <p style="color: white; font-size: 20px; font-weight: bold; margin: 5px 0;">{activite}</p>
        </div>
    </div>
    <div style="margin-top: 30px; font-size: 12px; color: #777;">
        Ce document certifie que le cerveau de l'utilisateur est officiellement en veille.<br>
        Validité : Jusqu'à la reprise (désolé).
    </div>
</div>
<style>
@keyframes slideUp {{
    from {{ transform: translateY(50px); opacity: 0; }}
    to {{ transform: translateY(0); opacity: 1; }}
}}
</style>
"""
        st.markdown(html_ticket, unsafe_allow_html=True)
