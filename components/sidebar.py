"""
components/sidebar.py
─────────────────────
Renders the sidebar input panel.
"""

import streamlit as st
from utils.encoders import CAR_NAMES


def render_sidebar() -> tuple:
    with st.sidebar:
        # ── Brand header ──────────────────────────────────
        st.markdown(
            "<div style='padding:8px 0 18px;'>"
            "<div style='font-family:Bebas Neue,sans-serif;font-size:2rem;"
            "letter-spacing:3px;color:#e8b84b;line-height:1;'>🚗 CarValue</div>"
            "<div style='font-size:0.72rem;letter-spacing:1.2px;color:#6b7899;"
            "text-transform:uppercase;margin-top:2px;'>Predictor · v1.0</div>"
            "</div>"
            "<hr style='border-color:rgba(232,184,75,0.14);margin-bottom:20px;'>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='font-size:0.8rem;color:#6b7899;margin-bottom:18px;'>"
            "Configure the car's specifications below, then hit "
            "<strong style='color:#e8b84b;'>Predict</strong>.</p>",
            unsafe_allow_html=True,
        )

        # ── Car Identity ──────────────────────────────────
        st.markdown("##### 🚘 Car Identity")
        car_name = st.selectbox("Car Model", CAR_NAMES,
                                index=CAR_NAMES.index("Maruti Swift"))
        year = st.slider("Year of Manufacture", min_value=2000,
                         max_value=2024, value=2017, step=1)
        st.divider()

        # ── Pricing & Usage ───────────────────────────────
        st.markdown("##### 💰 Pricing & Usage")
        present_price = st.number_input(
            "Present Showroom Price (₹ Lakhs)",
            min_value=0.10, max_value=150.0,
            value=5.59, step=0.10, format="%.2f",
        )
        kms_driven = st.number_input(
            "Kilometres Driven",
            min_value=100, max_value=600_000,
            value=27_000, step=500,
        )
        st.divider()

        # ── Specifications ────────────────────────────────
        st.markdown("##### ⚙️ Specifications")
        fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"], index=0)
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"], index=0)
        st.divider()

        # ── Ownership ─────────────────────────────────────
        st.markdown("##### 👤 Ownership")
        seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"], index=0)
        owner = st.selectbox(
            "Number of Previous Owners",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 — First Owner",
                1: "1 — Second Owner",
                2: "2 — Third Owner",
                3: "3 — Fourth Owner or More",
            }[x],
            index=0,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        predict_clicked = st.button("🔍  PREDICT PRICE", use_container_width=True)

        st.markdown(
            "<p style='font-size:0.7rem;color:#6b7899;text-align:center;margin-top:12px;'>"
            "Results are estimates. Actual prices may vary.</p>",
            unsafe_allow_html=True,
        )

    inputs = dict(
        car_name=car_name, year=year, present_price=present_price,
        kms_driven=kms_driven, fuel_type=fuel_type,
        transmission=transmission, seller_type=seller_type, owner=owner,
    )
    return inputs, predict_clicked
