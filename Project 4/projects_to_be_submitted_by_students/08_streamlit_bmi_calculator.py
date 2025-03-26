import streamlit as st
import pandas as pd

st.title("BMI Calculator") # Title

height = st.slider("Enter your Height (in cm):", 100,250,175)
weight = st.slider("Enter your Weight (in cm):", 40,200,75) # These are slider values

bmi = weight / (height/100)**2 

st.write("Your BMI is", bmi) # Display BMI without rounding
st.write(f"Your BMI with rounding off is {bmi:.0f}") # Display BMI with 2 decimal places

st.write("### BMI Categories ###")
st.write("Underweight: BMI less than 18.5")
st.write("Normal Weight: BMI Between 18.5 and 24.9")
st.write("Overweight: BMI Between 25 and 29.9")
st.write("Obese: BMI 30 or greater") # BMI categories