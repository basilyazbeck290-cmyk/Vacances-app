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
    
# --- 5. LA MAIN ROCK (Remplacement du cœur) ---
    # J'ai trouvé un dessin SVG de la main rock et j'ai remplacé le chemin du cœur.
    # J'ai aussi renommé la variable et l'animation pour que ce soit plus cohérent.

    html_hand = f"""
    <div style="display: flex; justify-content: center; margin-top: 30px; animation: rockPulse 1.5s infinite;">
        <svg width="250" height="250" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
            <path fill="{couleur_choisie}" d="M482.4 148.2c0-43.9-35.5-79.4-79.4-79.4-30.6 0-57.3 17.3-70.6 42.6-3.3-1-6.8-1.5-10.4-1.5-20 0-36.4 16.2-36.4 36.3 0 2.5 0.3 5.1 0.8 7.5-7.5-6-17-9.7-27.3-9.7-24 0-43.6 19.5-43.6 43.6 0 7.8 2.1 15.2 5.7 21.6-6.4-3.5-13.8-5.5-21.6-5.5-25.3 0-45.8 20.6-45.8 45.9v209.2h149.6c9.5 0 18.7-3.5 25.9-9.7l126.6-108.9c16.8-14.5 26.5-35.6 26.5-57.7V148.2zM193.8 42.3c0-23.4-19-42.3-42.3-42.3S109.2 19 109.2 42.3v205h-53v-33c0-10.8-8.8-19.6-19.6-19.6S17 203.6 17 214.3v84c0 31.1 12.1 61.1 34.2 83.1s52 34.2 83.1 34.2h30V42.3z"/>
        </svg>
    </div>
    <style>
    /* J'ai renommé l'animation 'heartbeat' en 'rockPulse' pour le style */
    @keyframes rockPulse {{
        0% {{ transform: scale(1) rotate(0deg); }}
        50% {{ transform: scale(1.1) rotate(5deg); }} /* Ajout d'une petite rotation stylée */
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
