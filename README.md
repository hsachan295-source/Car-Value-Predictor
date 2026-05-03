# 🚗 CarValue Predictor

🔗 **Live App:** https://car-value-predictor-syzumzqetpxap4hrcdrtcc.streamlit.app/

Instantly estimate the resale value of any used car using Machine Learning.
Built with a modular architecture and deployed on Streamlit Cloud.

---

## 📌 Overview

CarValue Predictor is a production-ready ML web application that predicts car resale prices based on multiple real-world features.

The model is optimized to reduce overfitting and provide reliable predictions on unseen data.

---

## 🧠 Model Details

| Property              | Value                   |
| --------------------- | ----------------------- |
| Algorithm             | Decision Tree Regressor |
| Library               | scikit-learn            |
| Hyperparameter Tuning | GridSearchCV            |
| Test R² Score         | ~0.84                   |
| Target                | Selling_Price (₹ Lakhs) |

---

## ⚙️ Features Used

* Present_Price
* Kms_Driven
* Owner
* Fuel_Type
* Seller_Type
* Transmission
* Year

---

## 🔢 Encoding Strategy

| Feature      | Encoding                  |
| ------------ | ------------------------- |
| Fuel_Type    | CNG=0, Diesel=1, Petrol=2 |
| Seller_Type  | Dealer=0, Individual=1    |
| Transmission | Automatic=0, Manual=1     |

---

## 🏗️ Project Structure

```bash id="n7h5b2"
CarValuePredictor/
│
├── app.py
├── final_model.pkl
├── requirements.txt
├── README.md
│
├── utils/
│   ├── __init__.py
│   ├── styles.py
│   ├── model_loader.py
│   └── encoders.py
│
└── components/
    ├── __init__.py
    ├── sidebar.py
    ├── hero.py
    ├── stats.py
    ├── predictor.py
    ├── info.py
    └── footer.py
```

---

## ✨ Key Features

* 🎨 Modern dark automotive UI
* ⚡ Fast performance using cached model loading
* 📊 Insight cards (vehicle age, depreciation, etc.)
* 🎯 Real-time prediction with clean output
* 🧩 Modular code structure (components + utils)
* 📱 Fully responsive Streamlit layout

---

## 🚀 Run Locally

```bash id="p7q4jm"
git clone https://github.com/hsachan295-source/Car-Value-Predictor.git

cd Car-Value-Predictor

python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**.

### Steps:

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Select repository
4. Set:

   * Branch: `main`
   * File: `app.py`
5. Click **Deploy**

---

## 📦 Requirements

```txt id="d2k9h1"
streamlit
scikit-learn
pandas
numpy
```

---

## ⚠️ Important Notes

* `final_model.pkl` must be present in root directory
* Feature encoding must match training phase
* Input order must remain consistent

---

## 💡 Future Improvements

* Add Random Forest / XGBoost model
* Add model comparison dashboard
* Integrate real-time car dataset APIs
* Improve UI with charts & analytics

---

## 👨‍💻 Author

**Harsh Sachan**
🎓 B.Tech CSE (AI)
🔗 https://github.com/hsachan295-source

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
