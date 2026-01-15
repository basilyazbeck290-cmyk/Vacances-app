import streamlit as st
import time
import base64 # <--- N'oublie pas cet import !

def jouer_musique_locale(fichier_audio):
    """Lit un fichier audio local en arrière-plan (invisible)"""
    # On lit le fichier binaire
    with open(fichier_audio, "rb") as f:
        data = f.read()
    # On encode en base64 pour que le navigateur comprenne
    b64 = base64.b64encode(data).decode()
    # On injecte le HTML
    md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Libération Janvier", page_icon="❄️", layout="centered")

# CSS : Fond sombre, couleurs et... LA NEIGE ❄️
st.markdown("""
    <style>
    /* --- TON CSS ORIGINAL --- */
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
    /* J'ai gardé ton style de bouton, il s'adaptera à la colonne */
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

    /* --- EFFET NEIGE --- */
    .snowflake {
        color: #fff;
        font-size: 1.5em;
        font-family: Arial;
        text-shadow: 0 0 1px #000;
        position: fixed;
        top: -10%;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation-name: snowflakes-fall, snowflakes-shake;
        animation-duration: 10s, 3s;
        animation-timing-function: linear, ease-in-out;
        animation-iteration-count: infinite, infinite;
    }
    
    @keyframes snowflakes-fall {
        0% { top: -10%; }
        100% { top: 100%; }
    }
    @keyframes snowflakes-shake {
        0% { transform: translateX(0px); }
        50% { transform: translateX(80px); }
        100% { transform: translateX(0px); }
    }

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


# --- 2. LE FORMULAIRE ---
st.title("❄️ Check-out : Session Janvier")
st.write("Formalités de sortie avant la pause bien méritée")

col1, col2 = st.columns(2)

with col1:
    prenom = st.text_input("Ton Prénom :", placeholder="Ex: Basil")
    
    # --- MODIFICATION ICI : Slider Émotionnel ---
    options_batterie = [
        "1% (Critique 💀)", 
        "20% (Au bout du rouleau 😫)", 
        "40% (Fragile 🫤)", 
        "60% (Stable 😐)", 
        "80% (En forme 😁)", 
        "100% (Machine de guerre 🚀)"
    ]
    
    batterie = st.select_slider(
        "Niveau de batterie actuel :", 
        options=options_batterie,
        value="20% (Au bout du rouleau 😫)"
    )

with col2:
    activite = st.selectbox("Objectif prioritaire :", 
                             ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon Séries 📺", "Aller skier ⛷️"])
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")

st.write("")
st.write("") # Un peu d'espace

# --- 3. LE BOUTON CENTRÉ ---
# Astuce : On crée 3 colonnes [petite, grande, petite] et on met le bouton au milieu
c_left, c_center, c_right = st.columns([1, 2, 1])

with c_center:
    bouton_clique = st.button("ACTIVER LE MODE VACANCES 🚀")

if bouton_clique:
    
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # 1. Petite animation de chargement
        barre = st.progress(0, text="Sauvegarde des neurones restants...")
        for i in range(100):
            time.sleep(0.01)
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        
        # 2. On lance les ballons
        st.balloons()
        
        # 3. D'ABORD on prépare et affiche le ticket (Code sorti du try/except)
        html_ticket = f"""
        <div style="font-family: Arial, sans-serif; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; margin-top: 10px; box-shadow: 0 0 25px {couleur_choisie}50; position: relative; overflow: hidden; animation: slideUp 0.8s ease-out;">
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
                <div style="flex: 1;">
                    <p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">État des lieux</p>
                    <p style="color: white; font-size: 16px; font-weight: bold; margin: 5px 0;">{batterie}</p>
                </div>
                <div style="font-size: 30px; padding: 0 10px;">✈️</div>
                <div style="flex: 1;">
                    <p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Destination</p>
                    <p style="color: white; font-size: 18px; font-weight: bold; margin: 5px 0;">{activite}</p>
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

        # 4. ENSUITE on lance la musique (indépendant du ticket)
        try:
            # Assure-toi que le fichier s'appelle bien exactement comme ça sur GitHub
            jouer_musique_locale("Layla.mp3") 
        except FileNotFoundError:
            st.error("Le fichier Layla.mp3 est introuvable (vérifie le nom exact sur GitHub) !")
