"""
components/predictor.py
───────────────────────
Renders the two-column prediction panel:
  Left  → Input summary table
  Right → Prediction result card (or placeholder)
"""

import streamlit as st
import numpy as np
from utils.encoders import build_feature_vector


def _summary_row(label: str, value: str) -> str:
    return (
        "<div style='display:flex;justify-content:space-between;align-items:center;"
        "padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:0.875rem;'>"
        f"<span style='color:#6b7899;'>{label}</span>"
        f"<span style='font-weight:500;color:#dde2ef;'>{value}</span>"
        "</div>"
    )


def _render_result(predicted_price: float, present_price: float, year: int):
    """Render the animated result card + insight metrics."""
    depreciation = (
        max(0.0, (present_price - predicted_price) / present_price * 100)
        if present_price > 0 else 0.0
    )
    age = 2024 - year

    card_html = (
        "<div style='background:linear-gradient(135deg,#131a13,#0f1a1a);"
        "border:1.5px solid #3ecf8e;border-radius:16px;padding:36px 32px;"
        "text-align:center;box-shadow:0 0 48px rgba(62,207,142,0.14);'>"
        "<div style='font-size:0.78rem;text-transform:uppercase;letter-spacing:2.5px;"
        "color:#3ecf8e;margin-bottom:10px;'>✅ Estimated Resale Value</div>"
        "<div style='font-family:Bebas Neue,sans-serif;"
        "font-size:clamp(2.8rem,6vw,4.4rem);color:#ffffff;"
        f"letter-spacing:2px;line-height:1;'>&#8377; {predicted_price:.2f}</div>"
        "<div style='font-size:1rem;color:#6b7899;margin-top:8px;'>"
        "Lakhs (Indian Rupees)</div>"
        "</div>"
    )
    st.markdown(card_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    m1.metric(
        "📉 Depreciation",
        f"{depreciation:.1f}%",
        delta=f"-₹{max(0, present_price - predicted_price):.2f}L",
        delta_color="inverse",
    )
    m2.metric("🗓️ Vehicle Age", f"{age} yr{'s' if age != 1 else ''}")
    m3.metric("📊 Value Retention", f"{max(0.0, 100 - depreciation):.1f}%")


def _render_placeholder():
    html = (
        "<div style='background:#13161f;border:1.5px dashed rgba(232,184,75,0.2);"
        "border-radius:16px;padding:48px 24px;text-align:center;'>"
        "<div style='font-size:3.5rem;margin-bottom:12px;'>🔍</div>"
        "<div style='color:#6b7899;font-size:0.88rem;line-height:1.7;'>"
        "Configure the car details in the sidebar<br>"
        "and click <strong style='color:#e8b84b;'>Predict Price</strong> "
        "to see the estimated resale value."
        "</div>"
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def render_predictor(model, inputs: dict, predict_clicked: bool):
    left, right = st.columns([1, 1], gap="large")

    # ── Left: Input summary ────────────────────────────────────────────
    with left:
        st.markdown(
            "<h3 style='font-family:Bebas Neue,sans-serif;letter-spacing:2px;"
            "color:#e8b84b;font-size:1.5rem;margin-bottom:14px;'>"
            "📋 Input Summary</h3>",
            unsafe_allow_html=True,
        )

        rows = (
            _summary_row("🚘 Car Model",        inputs["car_name"])
            + _summary_row("📅 Year",           str(inputs["year"]))
            + _summary_row("💰 Present Price",  f"&#8377; {inputs['present_price']:.2f} Lakhs")
            + _summary_row("🛣 Kms Driven",     f"{inputs['kms_driven']:,} km")
            + _summary_row("⛽ Fuel Type",       inputs["fuel_type"])
            + _summary_row("⚙ Transmission",    inputs["transmission"])
            + _summary_row("🏢 Seller Type",     inputs["seller_type"])
            + _summary_row("👤 Prev. Owners",   str(inputs["owner"]))
        )

        st.markdown(
            "<div style='background:#13161f;border:1px solid rgba(232,184,75,0.12);"
            f"border-radius:12px;padding:8px 18px;'>{rows}</div>",
            unsafe_allow_html=True,
        )

    # ── Right: Result ─────────────────────────────────────────────────
    with right:
        st.markdown(
            "<h3 style='font-family:Bebas Neue,sans-serif;letter-spacing:2px;"
            "color:#e8b84b;font-size:1.5rem;margin-bottom:14px;'>"
            "🎯 Prediction Result</h3>",
            unsafe_allow_html=True,
        )

        if predict_clicked:
            try:
                features = build_feature_vector(
                    car_name=inputs["car_name"],
                    year=inputs["year"],
                    present_price=inputs["present_price"],
                    kms_driven=inputs["kms_driven"],
                    fuel_type=inputs["fuel_type"],
                    seller_type=inputs["seller_type"],
                    transmission=inputs["transmission"],
                    owner=inputs["owner"],
                )
                price = float(model.predict(features)[0])
                price = max(0.0, price)
                _render_result(price, inputs["present_price"], inputs["year"])

            except Exception as exc:
                st.error(f"⚠️ Prediction failed: {exc}")
        else:
            _render_placeholder()

    # ── Divider ────────────────────────────────────────────────────────
    st.markdown(
        "<div style='height:2px;"
        "background:linear-gradient(90deg,transparent,rgba(255,255,255,0.06),transparent);"
        "margin:36px 0 24px;'></div>",
        unsafe_allow_html=True,
    )
