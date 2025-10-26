import streamlit as st
import joblib
import pandas as pd

st.title("💳 AI-Powered Fraud Detection System")

# Load saved model
model = joblib.load('fraud_detection_model.pkl')

st.subheader("Enter Transaction Details:")
features = st.text_area(
    "Enter comma-separated values (Time, V1-V28, Amount) - total 30 numbers:"
)

if st.button("Predict"):
    try:
        data = [float(x) for x in features.split(',')]
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        if prediction == 1:
            st.error(f"🚨 Fraudulent Transaction (Probability: {prob:.2%})")
        else:
            st.success(f"✅ Legitimate Transaction (Probability: {1 - prob:.2%})")
    except Exception as e:
        st.warning("⚠️ Please enter valid numeric input.")
        st.text(e)

