import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Save Model
model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")

st.write("Enter Patient information")
 
preg= st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("BloodPressure", min_value=0)
skin_thickness = st.number_input("SkinThickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):

    data = np.array([[
        preg,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Not Diabetic")

