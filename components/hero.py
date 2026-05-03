"""
components/hero.py
──────────────────
Renders the main page hero section: title, tagline, and gold divider.
"""

import streamlit as st


def render_hero():
    html = (
        "<div style='padding:10px 0 0;'>"
        "<div style='font-family:Bebas Neue,sans-serif;"
        "font-size:clamp(3.2rem,7vw,5.8rem);"
        "letter-spacing:4px;line-height:1.0;color:#e8b84b;"
        "text-shadow:0 0 80px rgba(232,184,75,0.2);'>"
        "🚗 CarValue Predictor"
        "</div>"
        "<p style='font-size:1rem;color:#6b7899;max-width:600px;"
        "line-height:1.75;margin:10px 0 0;'>"
        "Instantly estimate the <strong style='color:#dde2ef;'>resale value</strong> "
        "of any car using a machine-learning model trained on thousands of "
        "Indian car listings from the CarDekho dataset. "
        "Powered by a tuned <strong style='color:#dde2ef;'>Decision Tree Regressor</strong> "
        "with ~84% test accuracy."
        "</p>"
        "</div>"
        "<div style='height:2px;"
        "background:linear-gradient(90deg,transparent,#e8b84b 40%,transparent);"
        "margin:28px 0;'></div>"
    )
    st.markdown(html, unsafe_allow_html=True)
