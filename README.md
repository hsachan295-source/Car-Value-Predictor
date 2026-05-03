# 🚗 CarValue Predictor

> Instantly estimate the resale value of any Indian used car using Machine Learning.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

---

## 📁 Project Structure

```
CarValuePredictor/
│
├── app.py                  # Main Streamlit entry point
├── final_model.pkl         # Trained Decision Tree Regressor
├── requirements.txt        # Python dependencies
├── README.md
│
├── utils/
│   ├── __init__.py
│   ├── styles.py           # Global CSS (dark automotive theme)
│   ├── model_loader.py     # Cached model loading via pickle
│   └── encoders.py         # LabelEncoder maps + feature builder
│
└── components/
    ├── __init__.py
    ├── sidebar.py          # All input widgets
    ├── hero.py             # Page title + tagline
    ├── stats.py            # Four quick-stat cards
    ├── predictor.py        # Input summary + prediction result
    ├── info.py             # Expandable How-it-works + Feature Guide
    └── footer.py           # Branded footer
```

---

## ☁️ Deploy on Streamlit Cloud (Free — Recommended)

**Live link milega:** `https://share.streamlit.io/hsachan295-source/Car-Value-Predictor/main/app.py`

### Step 1 — GitHub Pe Push Karo
Pehle poora project GitHub repo mein upload karo (final_model.pkl bhi saath mein).

```bash
git add .
git commit -m "🚗 CarValue Predictor - ready for deployment"
git push origin main
```

### Step 2 — Streamlit Cloud Pe Login Karo
👉 [share.streamlit.io](https://share.streamlit.io) pe jao → **Sign in with GitHub**

### Step 3 — New App Deploy Karo
1. **"New app"** button click karo
2. Yeh fields bharo:

| Field | Value |
|---|---|
| Repository | `hsachan295-source/Car-Value-Predictor` |
| Branch | `main` |
| Main file path | `app.py` |

3. **"Deploy!"** click karo

### Step 4 — Wait Karo (~2-3 minutes)
Streamlit apne aap:
- Dependencies install karega (`requirements.txt` se)
- App build karega
- Live URL de dega ✅

> ⚠️ **Important:** `final_model.pkl` GitHub repo mein hona **zaroori** hai, tabhi Streamlit Cloud use kar payega.

---

## 🚀 Local Setup (Quick Start)

```bash
# 1. Repo clone karo
git clone https://github.com/hsachan295-source/Car-Value-Predictor.git
cd Car-Value-Predictor

# 2. Virtual environment banao (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Dependencies install karo
pip install -r requirements.txt

# 4. App run karo
streamlit run app.py
```

App opens at **http://localhost:8501** 🎉

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Decision Tree Regressor |
| Library | scikit-learn |
| Tuning | RandomizedSearchCV (100 iter, 5-fold CV) |
| Test R² | ~0.84 |
| Target | `Selling_Price` (₹ Lakhs) |
| Features | `Car_Name`, `Year`, `Present_Price`, `Kms_Driven`, `Fuel_Type`, `Seller_Type`, `Transmission`, `Owner` |

### Encoding (mirrors training `LabelEncoder`)

| Feature | Encoding |
|---|---|
| Fuel_Type | CNG=0, Diesel=1, Petrol=2 |
| Seller_Type | Dealer=0, Individual=1 |
| Transmission | Automatic=0, Manual=1 |
| Car_Name | Alphabetical index |

---

## ✨ Features

- **Dark automotive UI** — Bebas Neue + DM Sans, gold accent palette
- **Sidebar inputs** — all 8 model features with sensible defaults
- **Live input summary** — see your selections before predicting
- **Animated result card** — price displayed prominently in ₹ Lakhs
- **Insight metrics** — depreciation %, vehicle age, value retention
- **Expandable docs** — how it works + feature guide
- **Cached model loading** — fast reruns via `@st.cache_resource`
- **Error handling** — graceful messages for missing file / bad input

---

## 👤 Author

**Harsh Sachan** — CarValue Predictor v1.0