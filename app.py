import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('model/trained_model.sav', 'rb'))
scaler = pickle.load(open('model/scaler.sav', 'rb'))

# Title
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details to predict diabetes risk")

# Input fields (same order as dataset)
pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose Level", 0, 200, 100)
blood_pressure = st.number_input("Blood Pressure", 0, 150, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.number_input("Age", 1, 120, 30)

# Predict button
if st.button("Predict"):

    # input array
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    # scale input
    input_scaled = scaler.transform(input_data)

    # prediction
    prediction = model.predict(input_scaled)

    # output
    if prediction[0] == 1:
        st.error("⚠️ The person is DIABETIC")
    else:
        st.success("✅ The person is NOT diabetic")
