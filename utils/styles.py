"""
utils/styles.py
───────────────
Global CSS injection for CarValue Predictor.
"""

import streamlit as st


_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --bg:          #0b0d12;
    --surface:     #13161f;
    --surface2:    #1c2030;
    --surface3:    #232840;
    --accent:      #e8b84b;
    --accent-dim:  rgba(232,184,75,0.15);
    --accent-glow: rgba(232,184,75,0.35);
    --success:     #3ecf8e;
    --text:        #dde2ef;
    --muted:       #6b7899;
    --border:      rgba(232,184,75,0.14);
    --border-soft: rgba(255,255,255,0.06);
    --radius:      12px;
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stSidebar"] label {
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
}

input[type="number"],
[data-baseweb="input"] input,
[data-baseweb="select"] > div {
    background: var(--surface2) !important;
    color: var(--text) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
}

[data-testid="stMetric"] {
    background: var(--surface2) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: 10px !important;
    padding: 14px 18px !important;
}
[data-testid="stMetricLabel"] { color: var(--muted) !important; font-size: 0.78rem !important; }
[data-testid="stMetricValue"] { color: var(--text)  !important; font-size: 1.4rem !important; }

.stButton > button {
    background: var(--accent) !important;
    color: #0b0d12 !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.2rem !important;
    letter-spacing: 3px !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 14px 0 !important;
    width: 100% !important;
    box-shadow: 0 4px 22px var(--accent-glow) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    filter: brightness(1.12) !important;
    box-shadow: 0 6px 32px var(--accent-glow) !important;
    transform: translateY(-2px) !important;
}

[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius) !important;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--surface3); border-radius: 4px; }
</style>
"""


def inject_css():
    st.markdown(_CSS, unsafe_allow_html=True)
