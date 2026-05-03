"""
components/stats.py
───────────────────
Renders the four quick-stat cards shown below the hero.
"""

import streamlit as st


_STATS = [
    ("~84%",  "Test Accuracy (R²)"),
    ("8",     "Input Features"),
    ("DTR",   "Decision Tree Reg."),
    ("₹ INR", "Output Currency"),
]


def _card(value: str, label: str) -> str:
    return (
        "<div style='background:#13161f;border:1px solid rgba(232,184,75,0.15);"
        "border-radius:12px;padding:20px 16px;text-align:center;height:100%;'>"
        f"<div style='font-family:Bebas Neue,sans-serif;font-size:2.1rem;"
        f"color:#e8b84b;letter-spacing:1px;line-height:1;'>{value}</div>"
        f"<div style='font-size:0.72rem;color:#6b7899;text-transform:uppercase;"
        f"letter-spacing:1.2px;margin-top:6px;'>{label}</div>"
        "</div>"
    )


def render_stats():
    cols = st.columns(len(_STATS), gap="small")
    for col, (value, label) in zip(cols, _STATS):
        col.markdown(_card(value, label), unsafe_allow_html=True)

    st.markdown(
        "<div style='height:2px;"
        "background:linear-gradient(90deg,transparent,rgba(255,255,255,0.06),transparent);"
        "margin:28px 0;'></div>",
        unsafe_allow_html=True,
    )
