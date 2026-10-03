import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="PREDICTION OF REAL E-STATE PRICES", page_icon="🏠", layout="wide",)
st.markdown("""
<style>

.stApp {
    background-color: #F4F7FB;
}

/* Main title */
.main-title {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.main-title h1 {
    color: #1E3A8A;
    font-size: 38px;
    margin: 0;
}

.main-title p {
    color: #555555;
    font-size: 17px;
    margin-top: 8px;
}

/* Input section */
div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"] {
    background-color: #FFFFFF;
    padding: 10px;
    border-radius: 10px;
}

/* Predict button */
.stButton > button {
    width: 100%;
    background-color: #1E3A8A;
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 10px;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background-color: #2563EB;
    color: white;
}

/* Success prediction box */
div[data-testid="stAlert"] {
    border-radius: 10px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)
st.title("PREDICTION OF REAL E-STATE PRICES")
st.write("Enter the house characteristics to estimate the sale price in million RWF.")

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.sav")
model = load_model()

area=st.number_input("Area (m²)", 26.0, 426.4, 105.7)
bedrooms=st.number_input("Bedrooms", 1, 6, 3, step=1)
bathrooms=st.number_input("Bathrooms", 1, 5, 3, step=1)
age=st.number_input("House Age (years)", 0.4, 49.5, 6.8)
distance=st.number_input("Distance to City Centre (km)", 0.7, 27.4, 3.2)
parking=st.number_input("Parking Spaces", 0, 3, 1, step=1)
neighborhood=st.selectbox("Neighborhood", [ 'Kigali City', 'Gasabo', 'Kicukiro', 'Nyarugenge', 'Musanze', 'Huye'])

if st.button("Predict"):
    row=pd.DataFrame([{"Area_m2":area,"Bedrooms":bedrooms,"Bathrooms":bathrooms,
    "House_Age_Years":age,"Distance_to_City_km":distance,
    "Parking_Spaces":parking,"Neighborhood":neighborhood}])
    price=model.predict(row)[0]
    st.success(f"Predicted house price: {price:.2f} million RWF")
