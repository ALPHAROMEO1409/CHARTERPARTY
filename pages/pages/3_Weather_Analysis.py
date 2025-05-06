import streamlit as st
import pandas as pd

st.title("🌦️ Weather Data Analysis")

weather_file = st.file_uploader("Upload Weather File", type=["csv", "xlsx"])
if weather_file:
    weather_df = pd.read_csv(weather_file) if weather_file.name.endswith(".csv") else pd.read_excel(weather_file)
    st.write("### Preview", weather_df.head())
