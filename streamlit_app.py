import streamlit as st
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://157.230.63.95:8000/predict/"  # Replace with your actual FastAPI endpoint

# Page title
st.title("Fraud Detection Prediction")

# Input form for transaction data
st.header("Enter Transaction Details")

# Input fields
transaction_data = {
    "TRANSACTION_ID": st.number_input("Transaction ID", min_value=0, step=1, value=709627),
    "TX_DATETIME": st.text_input("Transaction Date and Time (YYYY-MM-DD HH:MM:SS)", value="2018-06-14 00:00:57"),
    "CUSTOMER_ID": st.number_input("Customer ID", min_value=0, step=1, value=4512),
    "TERMINAL_ID": st.number_input("Terminal ID", min_value=0, step=1, value=4627),
    "TX_AMOUNT": st.number_input("Transaction Amount", min_value=0.0, step=0.01, value=80.25),
    "TX_TIME_SECONDS": st.number_input("Transaction Time in Seconds", min_value=0, step=1, value=6393657),  # Fixed
    "TX_TIME_DAYS": st.number_input("Transaction Time in Days", min_value=0, step=1, value=74),  # Fixed
    "TX_FRAUD": st.number_input("Fraud Flag (0 or 1)", min_value=0, max_value=1, step=1, value=0),
    "TX_FRAUD_SCENARIO": st.number_input("Fraud Scenario", min_value=0, step=1, value=0),
    "TX_DURING_WEEKEND": st.number_input("During Weekend (0 or 1)", min_value=0, max_value=1, step=1, value=0),
    "TX_DURING_NIGHT": st.number_input("During Night (0 or 1)", min_value=0, max_value=1, step=1, value=1),
    "CUSTOMER_ID_NB_TX_1DAY_WINDOW": st.number_input("Customer TX Count (1 Day Window)", min_value=0.0, step=0.01, value=1.0),
    "CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW": st.number_input("Customer Avg Amount (1 Day Window)", min_value=0.0, step=0.01, value=80.25),
    "CUSTOMER_ID_NB_TX_7DAY_WINDOW": st.number_input("Customer TX Count (7 Day Window)", min_value=0.0, step=0.01, value=11.0),
    "CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW": st.number_input("Customer Avg Amount (7 Day Window)", min_value=0.0, step=0.01, value=102.03),
    "CUSTOMER_ID_NB_TX_30DAY_WINDOW": st.number_input("Customer TX Count (30 Day Window)", min_value=0.0, step=0.01, value=66.0),
    "CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW": st.number_input("Customer Avg Amount (30 Day Window)", min_value=0.0, step=0.01, value=105.64),
    "TERMINAL_ID_NB_TX_1DAY_WINDOW": st.number_input("Terminal TX Count (1 Day Window)", min_value=0.0, step=0.01, value=3.0),
    "TERMINAL_ID_RISK_1DAY_WINDOW": st.number_input("Terminal Risk (1 Day Window)", min_value=0.0, step=0.01, value=0.0),
    "TERMINAL_ID_NB_TX_7DAY_WINDOW": st.number_input("Terminal TX Count (7 Day Window)", min_value=0.0, step=0.01, value=8.0),
    "TERMINAL_ID_RISK_7DAY_WINDOW": st.number_input("Terminal Risk (7 Day Window)", min_value=0.0, step=0.01, value=0.0),
    "TERMINAL_ID_NB_TX_30DAY_WINDOW": st.number_input("Terminal TX Count (30 Day Window)", min_value=0.0, step=0.01, value=28.0),
    "TERMINAL_ID_RISK_30DAY_WINDOW": st.number_input("Terminal Risk (30 Day Window)", min_value=0.0, step=0.01, value=0.0),
}

# Submit button
if st.button("Predict Fraud"):
    try:
        # Send data to FastAPI for prediction
        response = requests.post(FASTAPI_URL, json=transaction_data)
        
        # Process the response
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", None)
            
            # Display the prediction result
            st.write("### Prediction:")
            st.write("Fraud" if prediction == 1 else "Not Fraud")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to the FastAPI server: {e}")
