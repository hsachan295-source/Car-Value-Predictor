# 🚗 CarValue Predictor

> Instantly estimate the resale value of any Indian used car using Machine Learning.

---

## 📁 Project Structure

```
CarValuePredictor/
│
├── app.py                  # Main Streamlit entry point
├── final_model.pkl         # Trained Decision Tree Regressor  ← YOU PROVIDE THIS
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

## 🚀 Quick Start

```bash
# 1. Clone / unzip the project
cd CarValuePredictor

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your trained model in the root folder
cp /path/to/final_model.pkl .

# 5. Run the app
streamlit run app.py
```

The app opens at **http://localhost:8501** in your browser.

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
