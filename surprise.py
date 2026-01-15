import streamlit as st
import time
import base64
import random

# --- 1. FONCTIONS ET CACHE ---
@st.cache_data
def get_audio_base64(fichier_audio):
    with open(fichier_audio, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def jouer_musique_locale(fichier_audio):
    b64 = get_audio_base64(fichier_audio)
    md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# --- 2. CONFIGURATION & CSS ---
st.set_page_config(page_title="Check-out Janvier", page_icon="🎫", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .stTextInput > div > div > input { color: white; background-color: #262730; }
    p, label, .stMarkdown { color: white !important; }
    
    /* BOUTON STYLÉ */
    .stButton>button {
        width: 100%; height: 70px;
        background: linear-gradient(90deg, #FF007F, #6600FF);
        color: white; font-size: 20px; font-weight: bold;
        border: none; border-radius: 15px;
        transition: 0.4s; margin-top: 20px;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 0px 25px rgba(102, 0, 255, 0.6); }

    /* NEIGE */
    .snowflake {
        color: #fff; font-size: 1.5em; font-family: Arial; text-shadow: 0 0 1px #000;
        position: fixed; top: -10%; z-index: 9999; user-select: none; pointer-events: none;
        animation: snowflakes-fall 10s linear infinite, snowflakes-shake 3s ease-in-out infinite;
    }
    @keyframes snowflakes-fall { 0% { top: -10%; } 100% { top: 100%; } }
    @keyframes snowflakes-shake { 0% { transform: translateX(0px); } 50% { transform: translateX(80px); } 100% { transform: translateX(0px); } }
    
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
""", unsafe_allow_html=True)

# --- 3. INTERFACE ---
st.title("❄️ Check-out : Session Janvier")
st.write("Configure ton extraction vers la liberté.")

# Ligne 1 : Identité et Batterie
col1, col2 = st.columns(2)
with col1:
    prenom = st.text_input("Ton Prénom (Agent en fuite) :", placeholder="Ex: Basil")
    batterie = st.select_slider("État vital actuel :", 
        options=["💀 1% (HS)", "😫 20% (Eco)", "😐 50% (Stable)", "😁 80% (Charge)", "🚀 100% (Full)"],
        value="😫 20% (Eco)")

# Ligne 2 : Destination et Transport
with col2:
    activite = st.selectbox("Mission Prioritaire :", 
        ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon Netflix 📺", "Ski extrême ⛷️", "Plage Mentale 🏖️", "Fuite à l'étranger ✈️", "Apéro infini 🍻"])
    
    transport = st.selectbox("Moyen d'exfiltration :", 
        ["Téléportation", "Dos de Dragon", "Train Fantôme", "Fusée SpaceX", "Trotinette volée", "À la nage"])

# Ligne 3 : Options et Blacklist
c1, c2 = st.columns([1, 2])
with c1:
    couleur_choisie = st.color_picker("Couleur du Pass :", "#00FFFF")
with c2:
    interdits = st.multiselect("OBJETS STRICTEMENT INTERDITS :", 
                               ["Réunions Teams", "Tableaux Excel", "Le mot 'Urgent'", "Réveil matin", "Costume/Cravate", "Appels masqués"],
                               default=["Réunions Teams", "Tableaux Excel"])

# Bouton d'action
st.write("")
c_left, c_center, c_right = st.columns([1, 2, 1])
with c_center:
    bouton_clique = st.button("IMPRIMER LE BOARDING PASS 🚀")

# --- 4. LOGIQUE & TICKET ---
if bouton_clique:
    if not prenom:
        st.warning("⚠️ Identité requise pour l'exfiltration !")
    else:
        # Son et Animation
        try:
            jouer_musique_locale("Layla.mp3") 
        except:
            pass # On ignore silencieusement si pas de son, pour ne pas casser l'app
        
        barre = st.progress(0, text="Génération du ticket...")
        for i in range(100):
            time.sleep(0.015)
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        st.balloons()
        
        # Formatage de la liste des interdits pour le HTML
        liste_interdits_html = " • ".join(interdits) if interdits else "Aucun (T'es courageux)"
        num_vol = f"FLT-{random.randint(100,999)}"

        # HTML DU TICKET AMÉLIORÉ
        html_ticket = f"""
        <div style="font-family: 'Courier New', monospace; border: 2px dashed {couleur_choisie}; background: #1a1a1a; padding: 0; border-radius: 15px; margin-top: 20px; box-shadow: 0 0 30px {couleur_choisie}40; overflow: hidden; animation: slideUp 0.8s ease-out; color: white;">
            
            <div style="background: {couleur_choisie}; padding: 15px; text-align: center;">
                <h2 style="margin:0; color: #1a1a1a; font-weight: 900; letter-spacing: 4px; text-transform: uppercase;">BOARDING PASS</h2>
                <div style="font-size: 12px; color: #1a1a1a; font-weight: bold;">OFFICIAL RELEASE DOCUMENT</div>
            </div>

            <div style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
                    <div>
                        <div style="color: #888; font-size: 10px; text-transform: uppercase;">PASSENGER</div>
                        <div style="font-size: 24px; font-weight: bold; color: white;">{prenom}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: #888; font-size: 10px; text-transform: uppercase;">FLIGHT N°</div>
                        <div style="font-size: 24px; font-weight: bold; color: {couleur_choisie};">{num_vol}</div>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; margin-bottom: 20px; border-bottom: 1px solid #333; padding-bottom: 15px;">
                    <div>
                        <div style="color: #888; font-size: 10px; text-transform: uppercase;">DESTINATION</div>
                        <div style="font-size: 18px; color: white;">{activite}</div>
                    </div>
                    <div style="text-align: right;">
                         <div style="color: #888; font-size: 10px; text-transform: uppercase;">BATTERY STATUS</div>
                        <div style="font-size: 16px; color: white;">{batterie}</div>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <div>
                         <div style="color: #888; font-size: 10px; text-transform: uppercase;">TRANSPORT</div>
                         <div style="font-size: 16px; font-style: italic;">{transport}</div>
                    </div>
                    <div style="background: white; width: 50px; height: 50px; padding: 2px;">
                        <div style="background: black; width: 100%; height: 100%; opacity: 0.8;"></div>
                    </div>
                </div>

                <div style="background: #2d2d2d; padding: 10px; border-radius: 8px; border-left: 4px solid #ff4b4b; margin-top: 15px;">
                    <div style="color: #ff4b4b; font-size: 10px; font-weight: bold; text-transform: uppercase;">⛔ Security Alert / Zone Interdite</div>
                    <div style="font-size: 12px; color: #ddd; margin-top: 3px;">{liste_interdits_html}</div>
                </div>

            </div>
            
            <div style="background: white; height: 30px; margin: 10px 20px; background-image: linear-gradient(90deg, #000 50%, transparent 50%); background-size: 4px 100%;"></div>
            <div style="text-align: center; font-size: 10px; color: #555; padding-bottom: 10px;">{random.randint(1000000000,9999999999)}</div>

        </div>
        <style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
