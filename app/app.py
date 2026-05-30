import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Load model
model = pickle.load(open("models/churn_model.pkl", "rb"))

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }

    h1 {
        color: #00FFAA;
        text-align: center;
    }

    .stButton>button {
        background-color: #00FFAA;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Customer Churn Prediction System")

st.write("### Enter customer details below")

# Inputs
gender = st.selectbox("Gender", ["Female", "Male"])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["No", "Yes"])

dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (Months)", 0, 72)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])

monthly_charges = st.number_input("Monthly Charges")

total_charges = st.number_input("Total Charges")

# Convert inputs
gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone_service = 1 if phone_service == "Yes" else 0

# Prediction
if st.button("Predict Churn"):

    data = np.array([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone_service,
        0,0,0,0,0,0,0,0,0,
        monthly_charges,
        total_charges,
        0,
        0
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")