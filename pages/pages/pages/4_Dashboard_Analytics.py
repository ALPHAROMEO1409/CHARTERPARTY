import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📈 Analytics Dashboard")

df = st.session_state.get('summary_df')
if df is not None:
    try:
        st.subheader("Speed vs Wind Force")
        fig1 = px.scatter(df, x='wind_force', y='speed', title="Speed vs Wind Force")
        st.plotly_chart(fig1)

        st.subheader("Speed vs Wave Height")
        fig2 = px.scatter(df, x='wave_height', y='speed', title="Speed vs Wave Height")
        st.plotly_chart(fig2)

        st.subheader("CP Speed vs Actual Speed")
        fig3 = px.histogram(df, x=['Voyage Avg Speed (knots)', 'Good Wx Speed (knots)'], barmode='group')
        st.plotly_chart(fig3)
    except:
        st.warning("Required columns not found for plotting.")
else:
    st.info("Please upload data in Performance Calculation first.")
