"""
╔══════════════════════════════════════════════════════╗
║         CarValue Predictor — Main Entry Point        ║
║         Author : Harsh Sachan                        ║
║         Model  : Decision Tree Regressor (~84% R²)   ║
╚══════════════════════════════════════════════════════╝
"""

import streamlit as st
from utils.styles import inject_css
from utils.model_loader import load_model
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.stats import render_stats
from components.predictor import render_predictor
from components.info import render_info_section
from components.footer import render_footer

# ── Page config ──────────────────────────────────────
st.set_page_config(
    page_title="CarValue Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "CarValue Predictor | Built by Harsh Sachan",
    },
)

# ── Inject global CSS ─────────────────────────────────
inject_css()

# ── Load model (cached) ───────────────────────────────
model = load_model()

# ── Sidebar → collect inputs + predict button ─────────
inputs, predict_clicked = render_sidebar()

# ── Main panel ────────────────────────────────────────
render_hero()
render_stats()
render_predictor(model, inputs, predict_clicked)
render_info_section()
render_footer()
