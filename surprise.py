import streamlit as st
import time
import base64
import random

# --- 1. FONCTIONS TECHNIQUES (AUDIO & DESIGN) ---

@st.cache_data
def get_audio_base64(fichier_audio):
    """Transforme le MP3 en code lisible par le navigateur"""
    try:
        with open(fichier_audio, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def jouer_musique(fichier):
    """Joue la musique sans recharger la page"""
    b64 = get_audio_base64(fichier)
    if b64:
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

def generer_html_ticket(prenom, batterie, activite, transport, couleur, interdits):
    """
    C'est ici que la magie visuelle opère 🎨.
    On sépare le design du reste du code pour y voir plus clair.
    """
    num_vol = f"JAN-{random.randint(10,99)}"
    seat = f"{random.choice(['A','B','C','D','E','F'])}{random.randint(1,30)}"
    gate = f"G{random.randint(1,12)}"
    liste_interdits = " • ".join(interdits) if interdits else "NÉANT (Risqué...)"
    
    # Le gros bloc HTML est isolé ici
    html = f"""
    <div style="font-family: 'Courier New', monospace; border: 2px dashed {couleur}; background: #1a1a1a; border-radius: 15px; margin-top: 20px; box-shadow: 0 0 30px {couleur}40; overflow: hidden; animation: slideUp 0.8s ease-out; color: white;">
        
        <div style="background: {couleur}; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center;">
            <div style="color: #1a1a1a; font-weight: 900; letter-spacing: 2px; font-size: 20px;">BOARDING PASS</div>
            <div style="color: #1a1a1a; font-weight: bold;">Priority: HIGH</div>
        </div>

        <div style="padding: 20px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 25px;">
                <div>
                    <div style="color: #666; font-size: 10px; text-transform: uppercase;">PASSENGER NAME</div>
                    <div style="font-size: 26px; font-weight: bold; text-transform: uppercase; color: white;">{prenom}</div>
                </div>
                <div style="text-align: right;">
                    <div style="color: #666; font-size: 10px; text-transform: uppercase;">FLIGHT</div>
                    <div style="font-size: 26px; font-weight: bold; color: {couleur};">{num_vol}</div>
                </div>
            </div>

            <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
                <div style="flex: 1;">
                    <div style="color: #666; font-size: 10px;">DESTINATION</div>
                    <div style="font-size: 16px; font-weight: bold;">{activite}</div>
                </div>
                <div style="flex: 1; text-align: center;">
                    <div style="color: #666; font-size: 10px;">GATE</div>
                    <div style="font-size: 20px; font-weight: bold; color: {couleur};">{gate}</div>
                </div>
                <div style="flex: 1; text-align: right;">
                    <div style="color: #666; font-size: 10px;">SEAT</div>
                    <div style="font-size: 20px; font-weight: bold; color: {couleur};">{seat}</div>
                </div>
            </div>

            <div style="display: flex; justify-content: space-between; padding-bottom: 15px; border-bottom: 1px solid #333; margin-bottom: 15px;">
                <div>
                     <div style="color: #666; font-size: 10px;">MODE TRANSPORT</div>
                     <div style="font-size: 14px; font-style: italic;">{transport}</div>
                </div>
                <div style="text-align: right;">
                     <div style="color: #666; font-size: 10px;">BATTERY</div>
                    <div style="font-size: 14px;">{batterie}</div>
                </div>
            </div>

            <div style="background: rgba(255, 75, 75, 0.1); padding: 8px; border-radius: 5px; border-left: 3px solid #ff4b4b;">
                <div style="color: #ff4b4b; font-size: 9px; font-weight: bold; text-transform: uppercase;">⛔ ITEMS CONFISQUÉS A LA DOUANE</div>
                <div style="font-size: 11px; color: #ccc; margin-top: 2px;">{liste_interdits}</div>
            </div>
        </div>
        
        <div style="background: white; padding: 10px;">
            <div style="height: 25px; background-image: linear-gradient(90deg, #000 50%, transparent 50%); background-size: 3px 100%;"></div>
            <div style="text-align: center; color: black; font-size: 10px; margin-top: 5px; font-family: monospace;">{random.randint(100000000000,999999999999)}</div>
        </div>
    </div>
    <style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
    """
    return html

# --- 2. CONFIGURATION PAGE & CSS GLOBAL ---
st.set_page_config(page_title="Check-out Janvier", page_icon="🎫", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    /* Champs de saisie stylisés */
    .stTextInput input { color: white !important; background-color: #262730 !important; border: 1px solid #444; }
    .stSelectbox div[data-baseweb="select"] > div { background-color: #262730 !important; color: white; }
    p, label { color: #eee !important; }
    
    /* Bouton principal */
    .stButton>button {
        width: 100%; height: 60px;
        background: linear-gradient(45deg, #FF007F, #6600FF);
        color: white; font-size: 18px; font-weight: bold;
        border: none; border-radius: 12px;
        margin-top: 15px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(102,0,255,0.5); }
    </style>
""", unsafe_allow_html=True)

# --- 3. UI PRINCIPALE ---
st.title("❄️ Check-out : Session Janvier")

col1, col2 = st.columns(2)
with col1:
    prenom = st.text_input("Identité du passager :", placeholder="Ton Prénom")
    batterie = st.select_slider("Niveau d'énergie :", options=["1% 💀", "20% 😫", "50% 😐", "80% 😁", "100% 🚀"], value="20% 😫")
    couleur = st.color_picker("Thème du billet :", "#00FFFF")

with col2:
    activite = st.selectbox("Destination :", ["Hibernation 🐻", "Raclette 🧀", "Netflix & Chill 📺", "Ski ⛷️", "Soleil 🏖️"])
    transport = st.selectbox("Moyen de transport :", ["Téléportation", "Train", "Avion", "Dos de Dragon", "Catapulte"])
    interdits = st.multiselect("Zone Interdite (Blacklist) :", ["Excel", "Teams", "Réveil", "Cravate", "Le mot 'ASAP'"], default=["Excel", "Teams"])

# --- 4. ACTION ---
st.write("")
if st.button("GÉNÉRER MON PASS DE SORTIE 🚀"):
    if not prenom:
        st.warning("⚠️ Eh oh, on ne part pas sans nom !")
    else:
        # 1. Musique
        jouer_musique("Layla.mp3")
        
        # 2. Barre de chargement (Suspense...)
        with st.spinner("Impression du ticket en cours..."):
            time.sleep(2) # Juste pour le show
            
        # 3. Animation finale
        st.balloons()
        
        # 4. Appel de la fonction pour récupérer le HTML propre
        html_final = generer_html_ticket(prenom, batterie, activite, transport, couleur, interdits)
        st.markdown(html_final, unsafe_allow_html=True)
