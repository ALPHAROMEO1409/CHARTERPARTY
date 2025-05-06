import streamlit as st
import pandas as pd
from charterparty_calculator import calculate_performance

st.title("📊 Performance Calculation")

uploaded_file = st.file_uploader("Upload Noon Report (.csv or .xlsx)", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.write("### Preview of Data", df.head())

    result, summary = calculate_performance(df, st.session_state.get('vessel'))
    
    st.write("### Summary Table")
    st.dataframe(summary)

    csv = summary.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Summary CSV", csv, "performance_summary.csv", "text/csv")

    st.session_state['summary_df'] = summary
