import streamlit as st
import time
import base64

# --- 1. FONCTIONS BLINDÉES & CACHE (Optimisation Code 2) ---
@st.cache_data
def get_audio_base64(fichier_audio):
    """Lit et encode le fichier une seule fois pour le garder en mémoire."""
    try:
        with open(fichier_audio, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def jouer_musique_secure(fichier_audio):
    """Joue le son de manière sécurisée (ne plante pas si fichier absent)"""
    b64 = get_audio_base64(fichier_audio)
    if b64:
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    else:
        # Pas d'erreur fatale, juste un petit warning discret
        st.toast("⚠️ Audio introuvable (Layla.mp3), mais on décolle quand même !", icon="🔇")

# --- 2. CONFIGURATION & DESIGN (Le style Code 1) ---
st.set_page_config(page_title="Mission : Libération", page_icon="❄️", layout="centered")

# CSS : Fond sombre, Bouton Gradient, Neige
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .stTextInput > div > div > input { color: white; background-color: #262730; }
    div[data-baseweb="select"] > div { background-color: #262730; color: white; }
    p, label, h1, h2, h3 { color: white !important; }
    
    /* BOUTON STYLÉ (Code 1) */
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
    </style>

    <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div>
    <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div>
""", unsafe_allow_html=True)


# --- 3. INTERFACE (Version Humanisée) ---

st.title("❄️ Check-Out Session Janvier")
st.subheader("On prépare ton billet de sortie pour février ?")

# On utilise un container pour regrouper les infos de manière moins "grille"
with st.container():
    st.write("### 📝 Quelques détails avant de partir...")
    
    # Prénom avec un ton plus amical
    prenom = st.text_input("C'est pour quel nom le ticket ?", placeholder="Ton petit nom ici...")
    
    if prenom:
        st.write(f"Ok {prenom}, on s'occupe de tout. ✨")

    st.divider()

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.write("**🪫 Ton niveau d'énergie**")
        batterie = st.select_slider(
            "Franchement, comment tu te sens ?", 
            options=["💀 HS", "😫 Fatigué", "😐 Ça va", "😁 En forme", "🚀 Prêt à tout"],
            value="😫 Fatigué"
        )
        
        # Le petit "plus" humain : une réaction au choix
        if "💀" in batterie:
            st.caption("Oh... il était temps que ça s'arrête. Courage !")
        elif "🚀" in batterie:
            st.caption("Quelle énergie ! Tu vas tout casser.")

    with col2:
        st.write("**🌴 Ton projet secret**")
        activite = st.selectbox(
            "Ta priorité absolue ?", 
            ["Hibernation totale 🐻", "Raclette Party 🧀", "Marathon De Films 📺", "Aller skier ⛷️", "Fuite à l'étranger ✈️", "Apéro infini 🍻"]
        )
        
        transport = st.selectbox(
            "Tu t'en vas comment ?", 
            ["Téléportation", "À la nage", "Dos de Dragon", "Trottinette Électrique", "Tapis Volant", "Uber Copter", "Sur un vélo volé"]
        )


# Dictionnaire de réactions
reactions = {
    "💀 HS": {"msg": "Diagnostic : Mort clinique. Réanimation par perfusion de sieste conseillée", "color": "error"},
    "😫 Fatigué": {"msg": "Ordonnance : 3 jours de pyjama et interdiction de regarder tes mails", "color": "warning"},
    "😐 Ça va": {"msg": "État stable. Tu peux tenir encore 2h, après on ne garantit plus rien", "color": "info"},
    "😁 En forme": {"msg": "Anomalie détectée : Trop d'énergie pour un mois de Janvier. On surveille ça", "color": "success"},
    "🚀 Prêt à tout": {"msg": "On t'a reconnu, Elon Musk. Calme-toi sur les expresso, on est juste en janvier, pas sur Mars", "color": "success"}
}

# 2. On récupère les infos selon le slider
info = reaction.get(batterie)

# 3. On affiche ça proprement dans le "trou"
st.write(f"**{info['titre']}**")
if info['couleur'] == "error":
    st.error(info['phrase'])
elif info['couleur'] == "warning":
    st.warning(info['phrase'])
elif info['couleur'] == "success":
    st.success(info['phrase'])
else:
    st.info(info['phrase'])


# On rend le bouton moins "industriel"
st.write("---")
bt_left, bt_center, bt_right = st.columns([1, 2, 1])
with bt_center:
    # Changement du label pour quelque chose de plus excitant
    bouton_clique = st.button("Imprimer le boarding pass 🚀")


# --- 4. LOGIQUE D'ACTIVATION ---
if bouton_clique:
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # A. Musique (Sécurisée)
        jouer_musique_secure("Layla.mp3") 

        # B. Animation de chargement
        barre = st.progress(0, text="Connexion au paradis...")
        for i in range(100):
            time.sleep(0.01) 
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        
        # C. Ballons
        st.balloons()
        
        # D. Ticket HTML (Version 3 colonnes du Code 1, plus riche)
        html_ticket = f"""
<div style="font-family: Arial, sans-serif; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; margin-top: 10px; box-shadow: 0 0 25px {couleur_choisie}50; position: relative; overflow: hidden; animation: slideUp 0.8s ease-out;">
<div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">Session Janvier Terminée</div>
<h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px 0px {couleur_choisie};">PASS LIBERTÉ</h1>
<p style="color: #cccccc; font-size: 16px; margin-top: 5px; font-style: italic;">Valable exclusivement pour :</p>
<h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
<div style="border-top: 1px solid #555; margin: 20px 0;"></div>
            
<div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap;">
<div style="flex: 1; min-width: 100px;">
<p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Batterie</p>
<p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{batterie}</p>
</div>
<div style="font-size: 25px; padding: 0 10px;">✈️</div>
<div style="flex: 1; min-width: 100px;">
<p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Destination</p>
<p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{activite}</p>
</div>
<div style="font-size: 25px; padding: 0 10px;">🚀</div>
<div style="flex: 1; min-width: 100px;">
<p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Transport</p>
<p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{transport}</p>
</div>
</div>
            
<div style="margin-top: 30px; font-size: 12px; color: #777;">Ce document certifie que le cerveau de l'utilisateur est officiellement en veille<br>Validité : Jusqu'à la reprise (désolé)</div>
</div>
<style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
