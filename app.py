import streamlit as st
import math

# Page configuration
st.set_page_config(page_title="Coach Compass 3D", page_icon="⚽", layout="centered")
# --- CODE TO HIDE MENU AND LINK TO GITHUB ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QSob {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Extended list of managers with 3D coordinates and descriptions
COACHES_EXTENDED = [
    {
        "name": "Massimiliano Allegri", 
        "x": 5.0, "y": 1.0, "z": -8.0,    
        "desc": "The Realistic Conservative: only the result and intelligent management of moments matter to you."
        "image": "img/allegri.jpg"
    },
    {
        "name": "Antonio Conte", 
        "x": -2.0, "y": 9.0, "z": -7.0,  
        "desc": "The Authoritarian Jacobin: iron discipline, grueling work and zero tolerance for dissent."
        "image": "img/conte.jpg"
    },
    {
        "name": "Maurizio Sarri", 
        "x": -8.0, "y": 2.0, "z": 5.0,  
        "desc": "The Intransigent Revolutionary: the beautiful game and tactical dogma come first."
        "image": "img/sarri.jpg"
    },
    {
        "name": "Carlo Ancelotti", 
        "x": 8.0, "y": -4.0, "z": 0.0,  
        "desc": "The Aristocratic Liberal: you manage champions with empathy, authority and absolute freedom."
        "image": "img/ancelotti.jpg"
    },
    {
        "name": "Marcelo Bielsa", 
        "x": -8.0, "y": -6.0, "z": 6.0,  
        "desc": "The Romantic Anarchist: crazy, total, idealistic football, rebellious to any logic of power."
        "image": "img/bielsa.jpg"
    },
    {
        "name": "Gian Piero Gasperini", 
        "x": -4.0, "y": 8.0, "z": 7.0,  
        "desc": "The Commander of the Commune: suffocating pressing, working-class enhancement and an iron fist."
        "image": "img/gasperini.jpg"
    },
    {
        "name": "Pep Guardiola", 
        "x": -6.0, "y": 7.0, "z": 7.0,  
        "desc": "The Technocratic Planner: maniacal ball possession and total control of the game system."
        "image": "img/guardiola.jpg"
    },
    {
        "name": "Diego Simeone", 
        "x": 3.0, "y": 8.0, "z": -8.0,  
        "desc": "The Sovereign of the Trench: all-out defense, group identity and battle spirit."
        "image": "img/simeone.jpg"
    },
    {
        "name": "Zinedine Zidane", 
        "x": 3.0, "y": -2.0, "z": 3.0,  
        "desc": "The Enlightened Monarch: silent charisma, serene management and absolute respect for the locker room."
        "image": "img/zidane.jpg"
    },
    {
        "name": "José Mourinho", 
        "x": 8.0, "y": 9.0, "z": -6.0, 
        "desc": "The Commander of the Besieged Fortress: cynicism, psychological warfare, and stout defense to win against everyone."
        "image": "img/mourinho.jpg"
    },
    {
        "name": "Roberto de Zerbi", 
        "x": -7.0, "y": -1.0, "z": 5.0, 
        "desc": "The Revolutionary Visionary: absolute dogma of playing out from the back, expressive freedom, and total courage."
        "image": "img/dezerbi.jpg"
    },
    {
        "name": "Stefano Pioli", 
        "x": -1.0, "y": -3.0, "z": 4.0, 
        "desc": "The Empathetic Family Man: group cohesion, lightheartedness, and collective solidarity without authoritarian rigidity."
        "image": "img/pioli.jpg"
    },
    {
        "name": "Jurgen Klopp", 
        "x": -5.0, "y": 2.0, "z": 7.0, 
        "desc": "The Rock 'n' Roll Leader: furious gegenpressing, overwhelming empathy, and extremely high-intensity offensive mentality."
        "image": "img/klopp.jpg"
    },
    {
        "name": "Mikel Arteta", 
        "x": 3.0, "y": 6.0, "z": -1.0, 
        "desc": "The Technocrat of Arsenal: meticulous match control, attention to detail, and engineering-like organization."
        "image": "img/arteta.jpg"
    },
    {
        "name": "José Bordalas", 
        "x": 2.0, "y": 7.0, "z": -9.0, 
        "desc": "The Master of the Trench and Garra: low block, extreme athleticism, and uncompromising defensive pragmatism."
        "image": "img/bordalas.jpg"
    },
    {
        "name": "Hansi Flick", 
        "x": -6.0, "y": 1.0, "z": 9.0, 
        "desc": "The General Manager of Verticality: extremely high defensive line, suffocating pressing, and devastating forward drive."
        "image": "img/flick.jpg"
    },
    {
        "name": "Ruben Amorim", 
        "x": -4.0, "y": -1.0, "z": 5.0, 
        "desc": "The Modern Commander: rigid 3-4-2-1 organization, collaborative leadership, and extremely clear tactical ideas."
        "image": "img/amorim.jpg"
    },
    {
        "name": "Unai Emery", 
        "x": 1.0, "y": 6.0, "z": 0.0, 
        "desc": "The Press Room Tactician: chameleon-like, meticulous cup preparation, and pushed pragmatism."
        "image": "img/emery.jpg"
    },
    {
        "name": "Sean Dyche", 
        "x": 3.0, "y": 5.0, "z": -6.0, 
        "desc": "The Premier League Workhorse: classic 4-4-2, long balls, compact block, and trench resistance."
        "image": "img/dyche.jpg"
    },
    {
        "name": "Luis Enrique", 
        "x": -6.0, "y": 5.0, "z": 6.0, 
        "desc": "The Republican Manager: dogmatic ball possession, institutional rigor, and rejection of individualisms."
        "image": "img/enrique.jpg"
    },
    {
        "name": "Xabi Alonso", 
        "x": 2.0, "y": 4.0, "z": 6.0, 
        "desc": "The Elegant Architect: flawless transitions, pitch control, and modern, flexible offensive mentality."
        "image": "img/alonso.jpg"
    },
    {
        "name": "Claudio Ranieri", 
        "x": 6.0, "y": -2.0, "z": -1.0, 
        "desc": "The Wise Gentleman: elastic pragmatism, paternal management, and the ability to unite any locker room."
        "image": "img/ranieri.jpg"
    },
    {
        "name": "Paulo Fonseca", 
        "x": -5.0, "y": 0.0, "z": 6.0, 
        "desc": "Paulo Fonseca: constant search for clean passing, fluid build-up, and offensive vocation."
        "image": "img/gasperini.jpg"
    },
    {
        "name": "Mauricio Pochettino", 
        "x": -3.0, "y": -2.0, "z": 5.0, 
        "desc": "The Modern Trainer: high athletic intensity, youth development, and dynamic, associative football."
        "image": "img/pochettino.jpg"
    },
    {
        "name": "Thomas Tuchel", 
        "x": -1.0, "y": 3.0, "z": 5.0, 
        "desc": "The Tactical Professor: meticulous perfectionism, strategic chameleon-like behavior, and extremely high demands."
        "image": "img/tuchel.jpg"
    },
    {
        "name": "Enzo Maresca", 
        "x": -5.0, "y": 3.0, "z": 7.0, 
        "desc": "The Disciple of Pep: obsessive possession, positional micro-structures, and territorial dominance."
        "image": "img/maresca.jpg"
    },
    {
        "name": "Lionel Scaloni", 
        "x": 1.0, "y": -4.0, "z": 0.0, 
        "desc": "The Empathetic Chameleon: fraternal team spirit, emotional intelligence and absolute tactical pragmatism to adapt to any opponent."
        "image": "img/scaloni.jpg"
    },
    {
        "name": "Luis de la Fuente", 
        "x": -3.0, "y": -3.0, "z": 5.0, 
        "desc": "The Vertical Normalizer: possession without dogmas, fierce search for one-on-ones on the wings and calm, silent management."
        "image": "img/delafuente.jpg"
    },
    {
        "name": "Vincent Kompany", 
        "x": -6.0, "y": 2.0, "z": 8.0, 
        "desc": "The Relentless Innovator: extreme high pressing, dogmatic ball possession and unwavering belief in attacking principles."
        "image": "img/kompany.jpg"
    },
    {
        "name": "Sergio Conceicao", 
        "x": 3.0, "y": 8.0, "z": -3.0, 
        "desc": "The Combative Sergeant: relentless intensity, strong organization and a fierce, uncompromising competitive spirit."
        "image": "img/conceicao.jpg"
    }
]

# The 40 statements with weights for the three axes (X, Y, Z)
QUESTIONS = [
    {"text": "1. Winning while playing poorly gives no real satisfaction: the beauty of the game comes before the result.", "wx": -2, "wy": 0, "wz": 2},
    {"text": "2. The locker room is a strict hierarchy: the manager's word is law.", "wx": 0, "wy": 2, "wz": 0},
    {"text": "3. Playing out from the back on the ground must always be attempted, even at the cost of risking it.", "wx": -2, "wy": -1, "wz": 2},
    {"text": "4. When leading, the best thing to do is drop deep and defend the lead.", "wx": 2, "wy": 1, "wz": -3},
    {"text": "5. To win you don't need champions, but exasperated team organization.", "wx": -2, "wy": 1, "wz": 0},
    {"text": "6. Behavioral rules and schedules must be ironclad and severely punished if violated.", "wx": 0, "wy": 2, "wz": 0},
    {"text": "7. Football is simple: too many tactical schemes only risk stifling the players' talent.", "wx": 2, "wy": -1, "wz": -1},
    {"text": "8. Better to win 4-3 conceding goals than 1-0 speculating on the narrowest margin.", "wx": -1, "wy": -1, "wz": 3},
    {"text": "9. At the end of a career, only the trophies in the cabinet matter, not how the team was remembered.", "wx": 2, "wy": 0, "wz": -1},
    {"text": "10. The manager must be an empathetic and fraternal leader, not a drill sergeant.", "wx": 0, "wy": -2, "wz": 0},
    {"text": "11. Multi-billionaire transfer windows with sheikhs and investment funds are the only way to guarantee long-term victory.", "wx": 2, "wy": 0, "wz": 0},
    {"text": "12. In press conferences, the manager must always protect the team, taking responsibility and avoiding public controversy.", "wx": 0, "wy": -2, "wz": 0},
    {"text": "13. Conceding a goal from a set-piece or an individual error hurts more than any offensive shortcoming; defensive solidity comes first.", "wx": 1, "wy": 0, "wz": -2},
    {"text": "14. Ultra-offensive pressing and high aggression from the first minute are essential to strangle the opponent's build-up.", "wx": -2, "wy": 1, "wz": 2},
    {"text": "15. If a player breaks curfew or skips a meeting, they must be excluded from the decisive match without exception, even if they are the best player in the squad.", "wx": 0, "wy": 2, "wz": 0},
    {"text": "16. Massive turnover is a mistake: you must always rely on the regular starters to avoid losing automatisms.", "wx": -1, "wy": 1, "wz": 0},
    {"text": "17. I prefer to lose a final playing an offensive and courageous football rather than winning it by catenaccio.", "wx": -2, "wy": 0, "wz": 2},
    {"text": "18. The team's senior players must be consulted by the manager before making crucial decisions.", "wx": 0, "wy": -2, "wz": 0},
    {"text": "19. The excessive use of advanced statistics, video analysis, and GPS data risks extinguishing the instinct and creativity of footballers.", "wx": 1, "wy": -1, "wz": 0},
    {"text": "20. Sterile ball possession is only used to waste time; immediate verticalization and counter-attacks are much more effective.", "wx": 2, "wy": 0, "wz": -2},
    {"text": "21. A manager must shoulder media pressure and act as a shield against the fans' fierce criticisms.", "wx": 0, "wy": 1, "wz": 0},
    {"text": "22. Investing in youth academies always pays off more than buying ready-made but expensive players on the market.", "wx": -2, "wy": 0, "wz": 0},
    {"text": "23. Changing formations during the match or mirroring the opponent shows intelligence and flexibility.", "wx": 2, "wy": 0, "wz": 0},
    {"text": "24. Even in numerical inferiority or a difficult away match, you must never give up attacking and playing the game.", "wx": -1, "wy": 0, "wz": 2},
    {"text": "25. I demand the board players that fit my style of football and do not want a player that does not, even if they are individually very strong.", "wx": -2, "wy": 0, "wz": 0},
    {"text": "26. Smiling on the bench and excessive familiarity with players ruin the coach's authority; professional distance is required.", "wx": 0, "wy": 2, "wz": 0},
    {"text": "27. The important thing is winning, it doesn't matter if suffering for ninety minutes: history only remembers the lifted trophies.", "wx": 2, "wy": 0, "wz": -1},
    {"text": "28. A serene climate, based on dialogue and players' happiness on the pitch, is the true secret of great winning cycles.", "wx": 0, "wy": -2, "wz": 1},
    {"text": "29. Athletic condition and the ability to run more than the opponent matter much more than pure technique or formations.", "wx": -1, "wy": 1, "wz": 1},
    {"text": "30. When winning by a narrow margin in the final minutes, wasting time, breaking up play, and smart tactical fouls are a necessary art.", "wx": 2, "wy": 0, "wz": -2},
    {"text": "31. Football is a collective work of art: the goal of a great manager is to leave a historical mark through ideas.", "wx": -2, "wy": -1, "wz": 2},
    {"text": "32. Modern footballers need constant iron-fist discipline; as soon as you loosen your grip on authority, the team falls apart.", "wx": 0, "wy": 2, "wz": -1},
    {"text": "33. On the pitch, there are no opponents to respect sportingly, but enemies to intimidate and overwhelm with mental strength.", "wx": 1, "wy": 2, "wz": -2},
    {"text": "34. Football is a contact sport: making ruthless tactical fouls and letting opponents feel your studs from the first minute is essential.", "wx": 2, "wy": 1, "wz": -2},
    {"text": "35. Referee and media controversies are legitimate and necessary weapons to shift pressure and unify the environment.", "wx": 1, "wy": 2, "wz": -1},
    {"text": "36. If a player on the pitch ignores tactical instructions and chooses to rely solely on personal instinct, they deserve an immediate and severe reprimand.", "wx": 1, "wy": 2, "wz": 0},
    {"text": "37. Modern football requires pure speed: the golden rule is to play in one or two touches to speed up the maneuver and avoid mental lethargy.", "wx": -1, "wy": 0, "wz": 2},
    {"text": "38. It is better to put the players in their best position, rather than making your players learn your football phylosophy.", "wx": 2, "wy": -1, "wz": 0},
    {"text": "39. If I need to defend a goal in the last minutes I prefer bringing on a defender for an offensive player over suffering with the same scheme.", "wx": 2, "wy": 0, "wz": 2},
    {"text": "40. It is better to have a goalkeeper that can play from the back but is an average shotstopper than one that can't play with their feet but is strong between the sticks.", "wx": -1, "wy": 0, "wz": 1},       
]

# Mapping text options to numerical values (-2 to +2)
options_mapping = {
    "Strongly disagree": -2,
    "Disagree": -1,
    "Neutral": 0,
    "Agree": 1,
    "Strongly agree": 2
}

st.title("⚽ Coach Compass 3D")
st.markdown("Answer the **40 statements** to discover which football manager matches your tactical philosophy, locker room management style, and mindset!")

# Collect answers through radio buttons
user_answers = []
for i, q in enumerate(QUESTIONS):
    st.markdown(f"**{q['text']}**")
    ans = st.radio(
        f"Answer {i+1}", 
        ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"], 
        index=2, 
        key=f"q_{i}",
        label_visibility="collapsed"
    )
    user_answers.append(options_mapping[ans])
    st.write("")

# Submit button
if st.button("🏆 Calculate your dugout alter ego!", type="primary"):
    raw_x = 0.0
    raw_y = 0.0
    raw_z = 0.0

    # Calculate raw scores
    for idx, ans_val in enumerate(user_answers):
        q = QUESTIONS[idx]
        raw_x += ans_val * q["wx"]
        raw_y += ans_val * q["wy"]
        raw_z += ans_val * q["wz"]

    # Calculate theoretical maximum possible scores for normalization
    max_x = sum(2 * abs(q["wx"]) for q in QUESTIONS)
    max_y = sum(2 * abs(q["wy"]) for q in QUESTIONS)
    max_z = sum(2 * abs(q["wz"]) for q in QUESTIONS)

    # Prevent division by zero
    max_x = max(max_x, 1)
    max_y = max(max_y, 1)
    max_z = max(max_z, 1)

    # Strict normalization between -10 and +10
    user_x = 1.33 * round((raw_x / max_x) * 10, 2)
    user_y = 1.33 * round((raw_y / max_y) * 10, 2)
    user_z = 1.33 * round((raw_z / max_z) * 10, 2)

    if user_x > 10: 
        user_x = 10
    if user_y > 10: 
        user_y = 10
    if user_z > 10: 
        user_z = 10
    if user_x < -10: 
         user_x = -10
    if user_y < -10: 
         user_y = -10
    if user_z < -10: 
         user_z = -10


    # Find the closest manager using 3D Euclidean distance
    closest_coach = None
    min_distance = float('inf')

    for coach in COACHES_EXTENDED:
        dist = math.sqrt(
            (user_x - coach["x"])**2 + 
            (user_y - coach["y"])**2 + 
            (user_z - coach["z"])**2
        )
        if dist < min_distance:
            min_distance = dist
            closest_coach = coach

    # Display results
    st.balloons()
    st.success("Test completed successfully!")
    
    st.markdown(f"### 🎯 Your alter ego is: **{closest_coach['name']}**")
    st.image(closest_coach["image"], width=400)
    st.info(closest_coach["desc"])
    
    st.markdown("#### 📐 Your coordinates in 3D space (from -10 to +10):")
    col1, col2, col3 = st.columns(3)
    col1.metric("X-Axis (RigidTactics/PragmaticManagement)", f"{user_x:.2f}")
    col2.metric("Y-Axis (SelfManagment/Authority)", f"{user_y:.2f}")
    col3.metric("Z-Axis (Difensive/Offensive)", f"{user_z:.2f}")
