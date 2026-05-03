"""
utils/encoders.py
─────────────────
Encoding maps that mirror the LabelEncoder transformation applied
during model training (sklearn's LabelEncoder uses sorted/alphabetical
order by default).

Feature order expected by the model:
    ['Car_Name', 'Year', 'Present_Price', 'Kms_Driven',
     'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
"""

import numpy as np

# ── Categorical encoding maps (alphabetical = LabelEncoder default) ──

FUEL_MAP = {
    "CNG":    0,
    "Diesel": 1,
    "Petrol": 2,
}

SELLER_MAP = {
    "Dealer":     0,
    "Individual": 1,
}

TRANSMISSION_MAP = {
    "Automatic": 0,
    "Manual":    1,
}

# ── Car names present in the CardDekho training dataset ──
CAR_NAMES = sorted([
    "Maruti 800", "Maruti Alto", "Maruti Alto K10", "Maruti Swift",
    "Maruti Swift Dzire", "Maruti Baleno", "Maruti Vitara Brezza",
    "Maruti Ertiga", "Maruti Celerio", "Maruti WagonR", "Maruti Omni",
    "Maruti Ciaz", "Maruti Ritz", "Maruti S-Cross", "Maruti Ignis",
    "Hyundai i10", "Hyundai i20", "Hyundai Creta", "Hyundai Verna",
    "Hyundai Grand i10", "Hyundai Xcent", "Hyundai Santro",
    "Hyundai Tucson", "Hyundai Elantra",
    "Honda City", "Honda Amaze", "Honda Jazz", "Honda WR-V",
    "Honda Brio", "Honda CR-V",
    "Toyota Fortuner", "Toyota Innova", "Toyota Corolla Altis",
    "Toyota Etios", "Toyota Yaris", "Toyota Camry",
    "Ford EcoSport", "Ford Figo", "Ford Aspire", "Ford Endeavour",
    "Tata Nexon", "Tata Tiago", "Tata Tigor", "Tata Indica",
    "Tata Harrier", "Tata Hexa",
    "Renault Kwid", "Renault Duster", "Renault Triber",
    "Mahindra Scorpio", "Mahindra XUV500", "Mahindra Bolero",
    "Mahindra Thar", "Mahindra KUV100",
    "Volkswagen Polo", "Volkswagen Vento", "Volkswagen Tiguan",
    "Nissan Micra", "Nissan Terrano", "Nissan Kicks",
    "Skoda Rapid", "Skoda Octavia", "Skoda Superb",
    "Jeep Compass", "MG Hector",
    "Kia Seltos", "Kia Sonet",
    "Other",
])

# Build label map: name → encoded integer
CAR_NAME_MAP = {name: idx for idx, name in enumerate(CAR_NAMES)}


def build_feature_vector(
    car_name: str,
    year: int,
    present_price: float,
    kms_driven: int,
    fuel_type: str,
    seller_type: str,
    transmission: str,
    owner: int,
) -> np.ndarray:
    """
    Convert raw user inputs into a model-ready numpy array.

    Returns
    -------
    np.ndarray of shape (1, 8)
    """
    return np.array([[
        CAR_NAME_MAP.get(car_name, 0),      # Car_Name (encoded)
        year,                                # Year
        present_price,                       # Present_Price
        kms_driven,                          # Kms_Driven
        FUEL_MAP[fuel_type],                 # Fuel_Type (encoded)
        SELLER_MAP[seller_type],             # Seller_Type (encoded)
        TRANSMISSION_MAP[transmission],      # Transmission (encoded)
        owner,                               # Owner
    ]])
