import streamlit as st
import urllib.parse

# ---------------------------------------------------------
# MOBILE‑FRIENDLY BUTTON STYLES + BIG CODE BOX
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

    /* BIGGER CODE BOX */
    .big-code-box .stCodeBlock {
        font-size: 20px !important;
        padding: 22px !important;
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TRAIT DATA
# ---------------------------------------------------------
TRAITS = [
    "Driver", "Navigator", "Harmoniser",
    "Guardian", "Connector", "Analyst", "Catalyst"
]

TRAIT_DESCRIPTIONS = {
    "Driver": "Action-oriented, decisive, forward-moving.",
    "Navigator": "Strategic, structured, clarity-seeking.",
    "Harmoniser": "Emotionally attuned, peace-focused, relational.",
    "Guardian": "Protective, stabilising, dependable.",
    "Connector": "Community-minded, social, bridge-builder.",
    "Analyst": "Logical, detail-driven, pattern-focused.",
    "Catalyst": "Creative, energising, change-igniting."
}

# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------
def compare_two_traits(mine, theirs):
    if mine == theirs:
        return f"You both share {mine}, meaning your core rhythms align naturally."
    else:
        return (
            f"A {mine} interacting with a {theirs} creates a dynamic contrast. "
            "This can be complementary or challenging depending on context."
        )

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

st.markdown("---")

# ---------------------------------------------------------
# BIG COPY BOX STYLES (MUST BE ABOVE THE IF BLOCK)
# ---------------------------------------------------------
st.markdown("""
<style>

.big-code-box .stCodeBlock {
    font-size: 20px !important;
    padding: 20px !important;
    border-radius: 12px !important;
}

/* Make the copy icon bigger and button-like */
.big-code-box .stCodeBlock button {
    transform: scale(1.8);
    background: #4CAF50 !important;
    border-radius: 8px !important;
    padding: 6px 10px !important;
    border: none !important;
    margin-right: 12px !important;
}

/* Make the icon itself white */
.big-code-box .stCodeBlock button svg {
    fill: white !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# BIG MOBILE‑FRIENDLY COMPARE BUTTON (THIS CREATES compare_clicked)
# ---------------------------------------------------------
st.markdown('<div class="big-main-button">', unsafe_allow_html=True)
compare_clicked = st.button("Compare Traits")
st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# RESULTS + BIG COPY BOX (THIS MUST COME AFTER compare_clicked)
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
    st.header("Copilot Prompt (Copy & Paste)")

    # Build the prompt (NOW prompt exists)
    prompt = build_copilot_prompt(
        my_primary, my_secondary, my_background,
        other_primary, other_secondary, other_background
    )

    # Friendly banner
    st.markdown("""
        <div style="
            background:#4CAF50;
            padding:14px;
            border-radius:10px;
            color:white;
            font-size:18px;
            font-weight:600;
            text-align:center;
            margin-bottom:10px;
        ">
            Tap the copy icon in the box below 👇
        </div>
    """, unsafe_allow_html=True)

    # Enlarged code box with big copy icon
    st.markdown('<div class="big-code-box">', unsafe_allow_html=True)
    st.code(prompt, language="markdown")
    st.markdown('</div>', unsafe_allow_html=True)

    # Copilot button
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




# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("Built for The Age of Disconnection — Trait Mapping Tool")

