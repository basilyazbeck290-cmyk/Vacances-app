import streamlit as st
import time

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Bonnes Vacances !",
    page_icon="💖",
    layout="centered"
)

# Petit style pour centrer les choses et mettre le fond noir (comme votre original)
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    h1 {
        text-align: center;
        color: white;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF007F;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. TITRE ---
st.title("🎓 Fin des Exams 🎓")

# --- 3. LE CHOIX DE COULEUR (Remplace la palette Windows) ---
st.write("Personnalise ton cadeau :")
couleur_coeur = st.color_picker("Choisis la couleur du cœur", "#FF007F")

# --- 4. LE BOUTON MAGIQUE ---
if st.button("Lancer la surprise !"):
    
    # Barre de chargement pour le suspense
    progress_text = "Calcul des vacances en cours..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    my_bar.empty() # On efface la barre
    
    # Lâcher de ballons (Effet spécial Streamlit)
    st.balloons()
    
    # --- 5. LE CŒUR (Dessiné en HTML/CSS pour être compatible iPad) ---
    html_heart = f"""
    <div style="display: flex; justify-content: center; margin-top: 50px;">
        <svg width="300" height="300" viewBox="0 0 24 24">
            <path fill="{couleur_coeur}" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
    </div>
    """
    st.markdown(html_heart, unsafe_allow_html=True)

    # --- 6. LE TEXTE ---
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <h2 style="color: white; text-shadow: 2px 2px 0 #000;">Les examens sont (enfin),</h2>
        <h1 style="color: white; font-size: 50px; text-shadow: 2px 2px 0 #000;">FINIS !!!</h1>
        <br>
        <h3 style="color: {couleur_coeur};">Bonnes Vacances ❤️</h3>
    </div>
    """, unsafe_allow_html=True)
