"""
components/info.py
──────────────────
Renders the expandable How-it-works and Feature Guide sections.
"""

import streamlit as st


def render_info_section():
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.expander("📖 How does this work?"):
            st.markdown("""
**Model:** Decision Tree Regressor (sklearn)

**Dataset:** CarDekho — thousands of used-car listings across India.

**Training pipeline:**
1. Raw CSV loaded and inspected for nulls
2. Categorical columns encoded with `LabelEncoder`
3. 80 / 20 train-test split (`random_state=42`)
4. Baseline tree trained → overfit (100% train R²)
5. Hyperparameter tuning via `RandomizedSearchCV` (100 iterations, 5-fold CV)
6. Best estimator saved as `final_model.pkl`

**Test R²:** ~0.84
            """)

    with col2:
        with st.expander("📌 Feature Guide"):
            st.markdown("""
| Feature | Description |
|---|---|
| **Car Model** | Make and model name |
| **Year** | Year of manufacture |
| **Present Price** | Current showroom price (₹ Lakhs) |
| **Kms Driven** | Total odometer reading |
| **Fuel Type** | Petrol / Diesel / CNG |
| **Seller Type** | Dealer or Individual |
| **Transmission** | Manual or Automatic |
| **Owner** | Number of previous owners (0–3) |
            """)
