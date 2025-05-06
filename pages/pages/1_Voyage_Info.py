import streamlit as st
import pandas as pd

st.title("🧾 Vessel & Voyage Information")

with st.form("voyage_form"):
    st.subheader("Vessel Details")
    vessel_name = st.text_input("Vessel Name")
    imo = st.text_input("IMO Number")

    st.subheader("Voyage Details")
    voyage_no = st.text_input("Voyage Number")
    port_from = st.text_input("From Port")
    port_to = st.text_input("To Port")
    cosp = st.datetime_input("COSP Date & Time")
    eosp = st.datetime_input("EOSP Date & Time")

    st.subheader("Charter Party (CP) Details")
    cp_speed = st.number_input("Warranted Speed (kn)", step=0.1)
    cp_consumption = st.number_input("Warranted FO Consumption (MT/day)", step=0.1)

    st.subheader("Weather Definition")
    beaufort = st.selectbox("Beaufort Limit", list(range(1, 13)))
    wave_height = st.selectbox("Sig. Wave Height Limit (m)", [x * 0.25 for x in range(0, 21)])

    st.subheader("Exclusion Period")
    exclusion_text = st.text_area("List Excluded Periods (e.g. Bunkering, Canal transit)")

    submitted = st.form_submit_button("Save Inputs")

if submitted:
    st.success("✅ Inputs Saved for Session")
    st.session_state['vessel'] = {
        "vessel_name": vessel_name, "imo": imo, "voyage_no": voyage_no,
        "port_from": port_from, "port_to": port_to, "cosp": cosp, "eosp": eosp,
        "cp_speed": cp_speed, "cp_consumption": cp_consumption,
        "beaufort": beaufort, "wave_height": wave_height,
        "exclusion": exclusion_text
    }
