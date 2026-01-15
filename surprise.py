import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="La Libération", page_icon="🎓", layout="centered")

# CSS Amélioré (Style "Carte Gold")
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    /* Style des champs de texte */
    .stTextInput > div > div > input {
        color: black;
    }
    /* Le bouton principal */
    .stButton>button {
        width: 100%;
        height: 70px;
        background: linear-gradient(45deg, #FF007F, #FFD700); /* Dégradé Rose/Or */
        color: white;
        font-size: 22px;
        font-weight: bold;
        border: none;
        border-radius: 35px;
        transition: 0.4s;
        box-shadow: 0px 0px 20px rgba(255, 0, 127, 0.5);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 30px rgba(255, 215, 0, 0.8);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. LE QUESTIONNAIRE ---
st.title("🎓 Le Grand Verdict 🎓")
st.write("Les examens sont finis... mais il reste une dernière formalité administrative.")

col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Lucas")
    humeur = st.selectbox("Ton état actuel :", 
                          ["Épuisé(e) 😴", "Survolté(e) ⚡", "Libéré(e) 🕊️", "En mode zombie 🧟"])

with col2:
    programme = st.selectbox("Ton programme ce soir :", 
                             ["Dormir 12h d'affilée", "Une grosse fête 🎉", "Netflix & Chill 🍿", "Rien faire du tout"])
    couleur_choisie = st.color_picker("Couleur du diplôme :", "#FFD700")

st.write("")
st.write("")

# --- 3. LE BOUTON FINAL ---
if st.button("Générer mon rapport de fin d'année 🎁"):
    
    if not prenom:
        st.warning("⚠️ Hé ! Il faut mettre ton prénom pour avoir la surprise !")
    else:
        # Suspense...
        progress_text = "Analyse des résultats..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent in range(100):
            time.sleep(0.02)
            my_bar.progress(percent + 1, text="Impression du certificat officiel...")
        
        time.sleep(0.5)
        my_bar.empty()
        
        # --- 4. LA SURPRISE (Double effet) ---
        st.balloons() # Ballons
        time.sleep(1)
        st.snow()     # Neige (effet paillettes)

        # --- 5. LE DIPLÔME (HTML/CSS Avancé) ---
        # On insère les variables (prenom, humeur, etc) dans le texte HTML
        html_diploma = f"""
        <div style="
            border: 4px solid {couleur_choisie};
            padding: 30px;
            border-radius: 20px;
            background-color: rgba(255, 255, 255, 0.1);
            text-align: center;
            box-shadow: 0 0 30px {couleur_choisie};
            margin-top: 20px;
            animation: popIn 1s ease-out;
        ">
            <svg width="150" height="150" viewBox="0 0 24 24" style="margin-bottom: 20px;">
                <path fill="{couleur_choisie}" d="M12 2l-3 6-6 1 4.5 4L6 19l6-3 6 3-1.5-6 4.5-4-6-1-3-6z"/> 
                </svg>

            <h1 style="color: white; font-family: 'Times New Roman', serif; text-transform: uppercase; letter-spacing: 2px;">
                CERTIFICAT DE SURVIE
            </h1>
            
            <p style="color: #DDDDDD; font-size: 18px;">Décerné officiellement à</p>
            
            <h2 style="color: {couleur_choisie}; font-size: 50px; margin: 10px 0; text-shadow: 0 0 10px rgba(0,0,0,0.5);">
                {prenom}
            </h2>
            
            <hr style="border-color: {couleur_choisie}; opacity: 0.5; width: 50%; margin: 20px auto;">
            
            <p style="font-size: 20px; color: white;">
                A survécu aux examens en étant <strong>{humeur}</strong>.<br>
                Est autorisé(e) à commencer immédiatement :<br>
                <span style="font-size: 28px; font-weight: bold; color: {couleur_choisie};">{programme}</span>
            </p>
            
            <div style="margin-top: 30px; font-style: italic; color: #888;">
                Fait le 15 Janvier 2026 <br>
                Signature: <span style="font-family: 'Brush Script MT', cursive; font-size: 24px;">Le Comité des Vacances</span>
            </div>
        </div>

        <style>
        @keyframes popIn {{
            0% {{ transform: scale(0); opacity: 0; }}
            80% {{ transform: scale(1.05); opacity: 1; }}
            100% {{ transform: scale(1); }}
        }}
        </style>
        """
        
        st.markdown(html_diploma, unsafe_allow_html=True)
