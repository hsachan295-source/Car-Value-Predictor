"""
utils/model_loader.py
─────────────────────
Loads and caches the Decision Tree Regressor from final_model.pkl.
Streamlit's @st.cache_resource ensures the model is loaded only once
across all reruns/users — critical for performance.
"""

import pickle
import streamlit as st


@st.cache_resource(show_spinner="🔧 Loading prediction model…")
def load_model():
    """
    Load the serialised sklearn DecisionTreeRegressor.

    Returns
    -------
    sklearn.tree.DecisionTreeRegressor
        The trained model, ready for inference.

    Raises
    ------
    SystemExit
        Halts the Streamlit app with a user-friendly error message
        if the model file is missing or corrupt.
    """
    try:
        with open("final_model.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error(
            "❌ **Model file not found.**\n\n"
            "Place `final_model.pkl` in the same directory as `app.py` and restart."
        )
        st.stop()
    except Exception as exc:
        st.error(f"❌ **Failed to load model:** `{exc}`")
        st.stop()
