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
        time.sleep(0.05) # Un tout petit peu plus lent pour le suspense
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    my_bar.empty() # On efface la barre
    
    # Lâcher de ballons
    st.balloons()
    
    # --- 5. LE CŒUR ---
    html_heart = f"""
    <div style="display: flex; justify-content: center; margin-top: 30px; animation: heartbeat 1.5s infinite;">
        <svg width="250" height="250" viewBox="0 0 24 24">
            <path fill="{couleur_choisie}" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
    </div>
    <style>
    @keyframes heartbeat {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
    """
    st.markdown(html_heart, unsafe_allow_html=True)

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
