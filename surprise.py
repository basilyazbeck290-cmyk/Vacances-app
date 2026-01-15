import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Libération Janvier", page_icon="🥂", layout="centered")

# CSS : Fond sombre, Centrage et Effets
st.markdown("""
    <style>
    /* Fond noir global */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Centrage des titres */
    h1, p {
        text-align: center !important;
    }
    
    /* Couleurs du texte des inputs */
    .stTextInput > div > div > input {
        color: white;
        background-color: #262730;
    }
    label {
        color: white !important;
    }
    
    /* Le bouton stylé et centré */
    .stButton>button {
        width: 100%;
        height: 70px;
        background: linear-gradient(90deg, #FF007F, #6600FF);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
        border-radius: 35px; /* Plus rond */
        transition: 0.4s;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.5);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px rgba(102, 0, 255, 0.8);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. LE HEADER (Centré via CSS) ---
st.title("🥂 Check-out : Session Janvier")
st.write("Formalités de sortie avant la pause bien méritée.")
st.write("") # Espace

# --- 3. LE FORMULAIRE ---
col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Chloé")
    # Ajout de l'option "Survie critique"
    batterie = st.select_slider("Niveau de batterie actuel :", 
                                options=["1% (Survie critique 🆘)", "10% (Besoin de sommeil)", "20% (Éco)", "50% (Ça va)", "100% (Machine)"],
                                value="20% (Éco)")

with col2:
    activite = st.selectbox("Objectif prioritaire :", 
                             ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon Séries 📺", "Aller skier ⛷️", "Boire pour oublier 🍹"])
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")

st.write("")
st.write("")

# --- 4. LE BOUTON (Centré avec des colonnes) ---
# Astuce : On utilise 3 colonnes (vide, bouton, vide) pour centrer le bouton
c_vide1, c_btn, c_vide2 = st.columns([1, 2, 1])

with c_btn:
    bouton_clique = st.button("ACTIVER LE MODE VACANCES 🚀")

if bouton_clique:
    
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # Animation de chargement
        with st.spinner("Génération du QR Code de sortie..."):
            time.sleep(1.5) # Suspense
        
        # Effets
        st.balloons()
        st.toast(f"Félicitations {prenom} ! Tu es libre !", icon="🎉")
        
        # --- 5. LE TICKET FINAL (Avec QR Code et Design Pro) ---
        html_ticket = f"""
<div style="
    font-family: 'Helvetica Neue', Arial, sans-serif;
    border: 2px solid {couleur_choisie};
    background: linear-gradient(135deg, #121212 0%, #2a2a2a 100%);
    padding: 0;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 0 30px {couleur_choisie}40;
    position: relative;
    overflow: hidden;
    color: white;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
    animation: slideUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
">
    <div style="background: {couleur_choisie}; padding: 15px; text-align: center;">
        <h3 style="margin: 0; color: black; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">BOARDING PASS VACANCES</h3>
    </div>

    <div style="padding: 25px;">
        <div style="display: flex; justify-content: space-between; align-items: end;">
            <div>
                <p style="color: #888; font-size: 12px; text-transform: uppercase; margin-bottom: 5px;">Passager</p>
                <h2 style="margin: 0; font-size: 32px; text-shadow: 0 0 10px {couleur_choisie};">{prenom}</h2>
            </div>
            <div style="text-align: right;">
                <p style="color: #888; font-size: 12px; text-transform: uppercase; margin-bottom: 5px;">Date</p>
                <h4 style="margin: 0; font-size: 18px;">JAN 2026</h4>
            </div>
        </div>

        <div style="margin: 20px 0; border-top: 2px dashed #444;"></div>

        <div style="display: flex; justify-content: space-between;">
            <div>
                <p style="color: {couleur_choisie}; font-size: 11px; text-transform: uppercase; margin: 0;">État Batterie</p>
                <p style="font-size: 16px; font-weight: bold; margin-top: 2px;">{batterie}</p>
            </div>
            <div style="text-align: right;">
                <p style="color: {couleur_choisie}; font-size: 11px; text-transform: uppercase; margin: 0;">Destination</p>
                <p style="font-size: 16px; font-weight: bold; margin-top: 2px;">{activite}</p>
            </div>
        </div>

        <div style="margin-top: 25px; background: white; padding: 10px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
            <svg width="60" height="60" viewBox="0 0 100 100">
                <rect width="100" height="100" fill="white"/>
                <path d="M10 10h30v30h-30z M60 10h30v30h-30z M10 60h30v30h-30z M50 50h10v10h-10z M70 70h20v20h-20z M20 20h10v10h-10z M70 20h10v10h-10z M20 70h10v10h-10z" fill="black"/>
            </svg>
            <div style="color: black; text-align: right; flex-grow: 1; margin-left: 10px;">
                <p style="font-size: 10px; margin: 0; font-family: monospace;">SCAN APPROVED</p>
                <p style="font-size: 14px; font-weight: bold; margin: 0;">LIBRE ✅</p>
            </div>
        </div>
    </div>
</div>

<style>
@keyframes slideUp {{
    from {{ transform: translateY(100px); opacity: 0; }}
    to {{ transform: translateY(0); opacity: 1; }}
}}
</style>
"""
        st.markdown(html_ticket, unsafe_allow_html=True)
