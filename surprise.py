# --- 4. LOGIQUE D'ACTIVATION ---
if bouton_clique:
    if not prenom:
        st.warning("⚠️ Remplis ton prénom pour valider ton ticket !")
    else:
        # --- A. MUSIQUE ---
        try:
            jouer_musique_locale("Layla.mp3") 
        except FileNotFoundError:
            st.error("⚠️ Fichier Layla.mp3 introuvable")

        # --- B. ANIMATION ---
        barre = st.progress(0, text="Connexion au paradis...")
        for i in range(100):
            time.sleep(0.01) 
            barre.progress(i + 1)
        time.sleep(0.2)
        barre.empty()
        
        # --- C. BALLONS & TICKET ---
        st.balloons()
        
        # NOTE IMPORTANTE : Tout le HTML ci-dessous est collé à gauche
        # pour éviter que Streamlit ne le prenne pour du code.
        html_ticket = f"""
<div style="font-family: Arial, sans-serif; border: 3px dashed {couleur_choisie}; background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%); padding: 30px; border-radius: 15px; text-align: center; margin-top: 10px; box-shadow: 0 0 25px {couleur_choisie}50; position: relative; overflow: hidden; animation: slideUp 0.8s ease-out;">
<div style="background-color: {couleur_choisie}; color: black; font-weight: bold; padding: 5px 15px; display: inline-block; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; font-size: 14px;">Session Janvier Terminée</div>
<h1 style="color: white; margin: 0; font-size: 40px; text-transform: uppercase; letter-spacing: 3px; text-shadow: 2px 2px 0px {couleur_choisie};">PASS LIBERTÉ</h1>
<p style="color: #cccccc; font-size: 16px; margin-top: 5px; font-style: italic;">Valable exclusivement pour :</p>
<h2 style="color: white; font-size: 50px; margin: 10px 0;">{prenom}</h2>
<div style="border-top: 1px solid #555; margin: 20px 0;"></div>
<div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap;">
<div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Batterie</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{batterie.split(' ')[0]}</p></div>
<div style="font-size: 25px; padding: 0 10px;">✈️</div>
<div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Destination</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{activite}</p></div>
<div style="font-size: 25px; padding: 0 10px;">🚀</div>
<div style="flex: 1; min-width: 100px;"><p style="color: {couleur_choisie}; font-size: 12px; text-transform: uppercase; margin: 0;">Transport</p><p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{transport}</p></div>
</div>
<div style="margin-top: 30px; font-size: 12px; color: #777;">Ce document certifie que le cerveau de l'utilisateur est officiellement en veille.<br>Validité : Jusqu'à la reprise (désolé).</div>
</div>
<style> @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }} </style>
"""
        st.markdown(html_ticket, unsafe_allow_html=True)
