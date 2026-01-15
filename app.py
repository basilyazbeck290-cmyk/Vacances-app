import streamlit as st
import time

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Surprise !",  # J'ai aussi changé le titre de l'onglet pour ne pas spoil
    page_icon="🎁",
    layout="centered"
)

# Style CSS (Fond noir + Bouton rose)
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    h1 {
        text-align: center;
        color: white;
        font-family: 'Helvetica', sans-serif;
    }
    /* Style du bouton */
    .stButton>button {
        width: 100%;
        height: 60px;
        border-radius: 30px;
        font-size: 20px;
        font-weight: bold;
        background-color: #FF007F;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4da6;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. TITRE MYSTÉRIEUX ---
st.title("✨ Petite Surprise ✨")

# --- 3. LE CHOIX DE COULEUR (Mystère) ---
st.write("Avant de commencer, il faut la configurer :")
# ICI : On ne dit plus que c'est un coeur
couleur_choisie = st.color_picker("Quelle est ta couleur préférée ?", "#FF007F") 

st.write("") # Petit espace
st.write("") 

# --- 4. LE BOUTON MAGIQUE ---
if st.button("Voir la surprise 🎁"):
    
    # Barre de chargement
    progress_text = "Chargement de la surprise..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.015) # Un tout petit peu plus lent pour le suspense
        my_bar.progress(percent_complete + 1, text=progress_text)

    time.sleep(0.25)
    
    my_bar.empty() # On efface la barre
    
    # Lâcher de ballons
    st.balloons()
    
# --- 5. LA MAIN ROCK (CORRIGÉE 🤘) ---
    html_hand = f"""
    <div style="display: flex; justify-content: center; margin-top: 30px; animation: rockPulse 1.5s infinite;">
                <svg width="250" height="250" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                        <path fill="{couleur_choisie}" d="M150.4 295.2V80c0-13.3 10.7-24 24-24h24c13.3 0 24 10.7 24 24V295.2c0 22.3 25.6 35.1 43.3 21.7l12.3-9.4C298.7 292 320 304.7 320 328V80c0-13.3 10.7-24 24-24h24c13.3 0 24 10.7 24 24V358.2c0 22.3 25.6 35.1 43.3 21.7l12.3-9.4c20.5-15.6 41.7-2.9 41.7 20.3V448c0 53-43 96-96 96H96c-53 0-96-43-96-96V80c0-13.3 10.7-24 24-24h24c13.3 0 24 10.7 24 24V295.2c0 22.3 25.6 35.1 43.3 21.7l12.3-9.4c20.5-15.6 41.7-2.9 41.7 20.3z"/>
        </svg>
    </div>
    <style>
    @keyframes rockPulse {{
        0% {{ transform: scale(1) rotate(0deg); }}
        50% {{ transform: scale(1.1) rotate(5deg); }} /* Petite rotation pour le style */
        100% {{ transform: scale(1) rotate(0deg); }}
    }}
    </style>
    """
    st.markdown(html_hand, unsafe_allow_html=True)

    # --- 6. LE TEXTE (MODIFIABLE ICI) ---
    # Vous pouvez changer les phrases entre les guillemets ci-dessous
    ligne_1 = "Les examens sont (enfin)"
    ligne_2 = "FINIS !!"
    ligne_3 = "Bonnes vacances 🍹"

    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <h3 style="color: #DDDDDD; font-weight: normal; margin-bottom: 0;">{ligne_1}</h3>
        <h1 style="color: white; font-size: 60px; margin-top: 10px; margin-bottom: 10px; text-shadow: 0 0 10px {couleur_choisie};">
            {ligne_2}
        </h1>
        <h3 style="color: {couleur_choisie}; font-style: italic;">{ligne_3}</h3>
    </div>
    """, unsafe_allow_html=True)
