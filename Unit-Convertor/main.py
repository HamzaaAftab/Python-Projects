import streamlit as st
import pandas as pd
import requests
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()
currency_rates = CurrencyRates()

# App title and layout
st.set_page_config(page_title="Ultimate Unit Converter", layout="wide")
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
        .dark-mode {background-color: #1e1e1e; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Ultimate Unit Converter")
st.write("Convert anything to everything with ease!")

# Sidebar options
st.sidebar.title("⚙️ Settings")
mode = st.sidebar.radio("Select Mode:", ["Light Mode", "Dark Mode"])

if mode == "Dark Mode":
    st.markdown("<body class='dark-mode'>", unsafe_allow_html=True)
else:
    st.markdown("<body class='main'>", unsafe_allow_html=True)

# Conversion categories
categories = ["Length", "Weight", "Temperature", "Time", "Speed", "Currency", "Data Storage"]
choice = st.selectbox("Choose conversion type", categories)

# Conversion Logic
if choice == "Length":
    units = ["meters", "kilometers", "miles", "yards", "feet", "inches", "centimeters"]
elif choice == "Weight":
    units = ["grams", "kilograms", "pounds", "ounces", "tons"]
elif choice == "Temperature":
    temp_units = {"Celsius": "degC", "Fahrenheit": "degF", "Kelvin": "kelvin"}
    units = list(temp_units.keys())
elif choice == "Time":
    units = ["seconds", "minutes", "hours", "days", "weeks"]
elif choice == "Speed":
    units = ["meters per second", "kilometers per hour", "miles per hour", "knots"]
elif choice == "Currency":
    units = list(currency_rates.get_rates("USD").keys())
elif choice == "Data Storage":
    units = ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]

input_val = st.number_input("Enter value:", format="%.5f")
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

if choice == "Temperature":
    result = (input_val * ureg(temp_units[from_unit])).to(temp_units[to_unit])
elif choice == "Currency":
    result = currency_rates.convert(from_unit, to_unit, input_val)
elif choice == "Data Storage":
    result = (input_val * ureg(from_unit)).to(to_unit)
else:
    result = (input_val * ureg(from_unit)).to(to_unit)

st.success(f"{input_val} {from_unit} = {result.magnitude:.5f} {to_unit}")

# Save history feature
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Save Conversion"):
    st.session_state.history.append(f"{input_val} {from_unit} = {result.magnitude:.5f} {to_unit}")
    st.success("Conversion saved!")

st.sidebar.subheader("📜 History")
st.sidebar.write(st.session_state.history)
