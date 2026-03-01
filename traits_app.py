import streamlit as st
import urllib.parse

# ---------------------------------------------------------
# MOBILE-FRIENDLY BUTTON STYLES + BIG CODE BOX
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Main Compare Button */
    .big-main-button button {
        width: 100%;
        padding: 18px 0;
        font-size: 22px;
        font-weight: 600;
        border-radius: 12px;
        background-color: #0066CC;
        color: white;
        border: none;
    }
    .big-main-button button:hover {
        background-color: #0052a3;
    }

    /* Big Code Box */
    .big-code-box .stCodeBlock {
        font-size: 20px !important;
        padding: 20px !important;
        border-radius: 12px !important;
    }

    /* Open in Copilot Button */
    .copilot-btn a {
        display: block;
        text-align: center;
        width: 100%;
        padding: 16px 0;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        background-color: #7B3FE4;
        color: white !important;
        text-decoration: none;
    }
    .copilot-btn a:hover {
        background-color: #6a2fd1;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TRAIT DATA + MEANINGS
# ---------------------------------------------------------
TRAITS = [
    "Driver", "Navigator", "Harmoniser",
    "Guardian", "Connector", "Analyst", "Catalyst"
]

TRAIT_MEANINGS = {
    "Driver": "Drivers move fast, take charge, and create momentum. They bring direction and decisive energy.",
    "Navigator": "Navigators are strategic, steady, and thoughtful. They see the long game and guide others calmly.",
    "Harmoniser": "Harmonisers create emotional safety, connection, and warmth. They tune into people deeply.",
    "Guardian": "Guardians are grounded, reliable, and stabilising. They protect routines and bring consistency.",
    "Connector": "Connectors are expressive, social, and energising. They spark interaction and shared enthusiasm.",
    "Analyst": "Analysts are logical, precise, and structured. They bring clarity, rigour, and thoughtful reasoning.",
    "Catalyst": "Catalysts are intuitive, creative, and future-focused. They spark new ideas and unconventional paths."
}

def trait_meaning(trait):
    return TRAIT_MEANINGS.get(trait, "")

# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------
def compare_two_traits(mine, theirs):
    interactions = {
        ("Driver", "Navigator"):
            "Drivers bring momentum and decisive action, while Navigators bring structure and clarity. This pairing can achieve a huge amount when they respect each other's pace. The Driver may feel slowed down, and the Navigator may feel rushed, but together they create a powerful strategic engine.",
        
        ("Driver", "Harmoniser"):
            "Drivers push forward with urgency, while Harmonisers prioritise emotional balance and relational safety. This can create a grounding dynamic where the Harmoniser softens the Driver’s edges. If communication is poor, the Driver may feel held back and the Harmoniser may feel overwhelmed.",
        
        ("Driver", "Guardian"):
            "Drivers want speed and change, Guardians want stability and protection. This creates a natural tension between movement and caution. When aligned, the Driver brings progress and the Guardian ensures it’s sustainable and safe.",
        
        ("Driver", "Connector"):
            "Drivers focus on goals, Connectors focus on people. This pairing can create socially impactful momentum when they work together. The Driver may need to slow down for relational needs, while the Connector may need to stay focused on outcomes.",
        
        ("Driver", "Analyst"):
            "Drivers act quickly, Analysts think deeply. This can create a brilliant balance of speed and precision. The Analyst may feel pressured, and the Driver may feel slowed, but together they produce high‑quality results.",
        
        ("Driver", "Catalyst"):
            "Both are high‑energy, change‑oriented traits. This pairing is exciting, creative, and fast‑moving, but can become chaotic without grounding. They inspire each other but may struggle with consistency.",
        
        ("Navigator", "Harmoniser"):
            "Navigators bring clarity and structure, Harmonisers bring emotional intelligence and relational awareness. This creates a thoughtful, steady partnership. They naturally avoid conflict and build trust through calm communication.",
        
        ("Navigator", "Guardian"):
            "Both traits value stability, planning, and predictability. This is one of the most naturally aligned pairings in the model. They create a safe, organised environment but may need to invite more spontaneity.",
        
        ("Navigator", "Connector"):
            "Navigators organise ideas, Connectors organise people. Together they build strong communities with clear direction. The Navigator may need to soften rigidity, and the Connector may need to stay focused.",
        
        ("Navigator", "Analyst"):
            "Both traits are detail‑focused, logical, and structured. This pairing excels in problem‑solving and long‑term planning. They may need to consciously bring warmth or creativity into the dynamic.",
        
        ("Navigator", "Catalyst"):
            "Navigators plan, Catalysts innovate. This creates a dynamic tension between structure and spontaneity. When balanced, they produce visionary ideas with practical pathways.",
        
        ("Harmoniser", "Guardian"):
            "Both traits are protective, steady, and emotionally aware. This pairing creates a deeply safe and nurturing environment. They may need to push each other gently toward growth and change.",
        
        ("Harmoniser", "Connector"):
            "Warm, relational, and community‑focused — this is one of the most socially powerful pairings. They build trust quickly and create inclusive spaces. They may need help with boundaries or decision‑making.",
        
        ("Harmoniser", "Analyst"):
            "Emotion meets logic in this pairing. They can learn a huge amount from each other if they stay patient. The Harmoniser brings empathy, the Analyst brings clarity, and together they create balanced understanding.",
        
        ("Harmoniser", "Catalyst"):
            "Harmonisers stabilise, Catalysts energise. This can be inspiring, creative, and emotionally rich. The Harmoniser may feel overwhelmed by pace, and the Catalyst may feel slowed, but the growth potential is high.",
        
        ("Guardian", "Connector"):
            "Guardians stabilise, Connectors expand. This creates a grounded but socially rich dynamic. The Guardian offers protection, the Connector brings people together, and together they build strong communities.",
        
        ("Guardian", "Analyst"):
            "Both traits value clarity, reliability, and thoughtful decision‑making. This pairing is steady, dependable, and low‑drama. They may need to consciously invite creativity or emotional expression.",
        
        ("Guardian", "Catalyst"):
            "Guardians protect, Catalysts disrupt. This can be tense but also transformative. When they respect each other’s intentions, the Guardian ensures safety while the Catalyst drives innovation.",
        
        ("Connector", "Analyst"):
            "Connectors bring people, Analysts bring insight. This pairing is excellent for collaboration and communication. They balance emotional awareness with logical clarity.",
        
        ("Connector", "Catalyst"):
            "Both are expressive, creative, and people‑oriented. This pairing is lively, idea‑rich, and socially energising. They may need grounding to avoid over‑committing.",
        
        ("Analyst", "Catalyst"):
            "Analysts refine ideas, Catalysts generate them. This pairing can produce brilliant innovation when they stay open to each other’s styles. The Analyst brings structure, the Catalyst brings spark."
    }

    if mine == theirs:
        return f"Two {mine}s together amplify that trait’s strengths and blind spots. This creates a powerful shared rhythm, but also doubles the challenges associated with that trait. When self‑aware, this pairing becomes deeply effective."

    pair = (mine, theirs)
    reverse_pair = (theirs, mine)

    return interactions.get(pair) or interactions.get(reverse_pair) or \
        f"{mine} and {theirs} create a unique dynamic with complementary strengths and growth edges."


def build_copilot_prompt(
    my_primary, my_secondary, my_background,
    other_primary, other_secondary, other_background
):
    return f"""
Using the Seven Traits model from The Age of Disconnection, analyse the relationship dynamics between two people.

Person A:
- Primary: {my_primary}
- Secondary: {my_secondary}
- Background: {my_background}

Person B:
- Primary: {other_primary}
- Secondary: {other_secondary}
- Background: {other_background}

Please explain:
1. Core alignment or friction between their primary traits.
2. How their secondary traits influence collaboration, communication, and emotional rhythm.
3. How background traits shape long-term patterns.
4. Potential strengths, blind spots, and growth opportunities.
5. The overall 6-5 rhythm between them.

Write the response in a warm, psychologically insightful tone.
"""

# ---------------------------------------------------------
# APP UI
# ---------------------------------------------------------
st.title("Trait Comparison Tool — The Age of Disconnection")

# -------------------------
# YOUR TRAITS
# -------------------------
st.subheader("Your Traits")
my_primary = st.selectbox("Your Primary Trait", TRAITS, key="my_primary")
my_secondary = st.selectbox(
    "Your Secondary Trait",
    [t for t in TRAITS if t != my_primary],
    key="my_secondary"
)
my_background = st.selectbox(
    "Your Background Trait",
    [t for t in TRAITS if t not in [my_primary, my_secondary]],
    key="my_background"
)

# --- YOUR TRAIT MEANINGS ---
st.write("### Your Trait Meanings")
st.info(trait_meaning(my_primary))
st.info(trait_meaning(my_secondary))
st.info(trait_meaning(my_background))

# -------------------------
# THEIR TRAITS
# -------------------------
st.subheader("Their Traits")
other_primary = st.selectbox("Their Primary Trait", TRAITS, key="other_primary")
other_secondary = st.selectbox(
    "Their Secondary Trait",
    [t for t in TRAITS if t != other_primary],
    key="other_secondary"
)
other_background = st.selectbox(
    "Their Background Trait",
    [t for t in TRAITS if t not in [other_primary, other_secondary]],
    key="other_background"
)

# --- THEIR TRAIT MEANINGS ---
st.write("### Their Trait Meanings")
st.info(trait_meaning(other_primary))
st.info(trait_meaning(other_secondary))
st.info(trait_meaning(other_background))

st.markdown("---")

# ---------------------------------------------------------
# BIG MOBILE-FRIENDLY COMPARE BUTTON
# ---------------------------------------------------------
st.markdown('<div class="big-main-button">', unsafe_allow_html=True)
compare_clicked = st.button("Compare Traits")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# RESULTS + COPY + COPILOT
# ---------------------------------------------------------
if compare_clicked:
    st.header("Trait Comparison Summary")

    st.write("### Primary Trait Interaction")
    st.write(compare_two_traits(my_primary, other_primary))

    st.write("### Secondary Trait Interaction")
    st.write(compare_two_traits(my_secondary, other_secondary))

    st.write("### Background Trait Interaction")
    st.write(compare_two_traits(my_background, other_background))

    st.markdown("---")
    st.header("Copilot (Copy & Paste) you can press the copy button on the top right! or copy then press the co-pilot link ")

    prompt = build_copilot_prompt(
        my_primary, my_secondary, my_background,
        other_primary, other_secondary, other_background
    )

    # --- BIG CODE BOX WITH NATIVE COPY ---
    st.markdown('<div class="big-code-box">', unsafe_allow_html=True)
    st.code(prompt, language="markdown")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- COPILOT BUTTON ---
    encoded_prompt = urllib.parse.quote(prompt)
    copilot_url = f"https://copilot.microsoft.com/?q={encoded_prompt}"

    st.markdown(
        f'<div class="copilot-btn"><a href="{copilot_url}" target="_blank">Open in Copilot</a></div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("Built for The Age of Disconnection — Trait Mapping Tool")