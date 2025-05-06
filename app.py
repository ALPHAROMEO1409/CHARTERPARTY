import streamlit as st

st.set_page_config(
    page_title="Charter Party Performance Suite",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1606220633217-f06f5f5d2787");
            background-size: cover;
        }
        .title {
            font-size:48px;
            color:#fff;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🚢 Charter Party Performance Monitoring</p>', unsafe_allow_html=True)
st.markdown("Use the left sidebar to navigate through the modules.")
