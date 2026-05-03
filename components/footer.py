"""
components/footer.py
────────────────────
Renders the branded footer.
"""

import streamlit as st


def render_footer():
    st.markdown(
        "<div style='margin-top:60px;padding:22px 0 12px;"
        "border-top:1px solid rgba(232,184,75,0.12);text-align:center;"
        "font-size:0.8rem;color:#6b7899;letter-spacing:0.4px;'>"
        "Built with ❤️ by&nbsp;"
        "<strong style='color:#e8b84b;'>Harsh Sachan</strong>"
        "&nbsp;·&nbsp;"
        "Powered by <strong style='color:#dde2ef;'>Scikit-learn</strong>"
        " &amp; <strong style='color:#dde2ef;'>Streamlit</strong>"
        "&nbsp;·&nbsp;CarValue Predictor v1.0"
        "</div>",
        unsafe_allow_html=True,
    )
