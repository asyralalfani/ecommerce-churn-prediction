"""
Streamlit UI for E-commerce Churn Prediction
"""

import streamlit as st
import requests
import os

# Page configuration
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="🎯",
    layout="wide"
)

# Title
st.title("🎯 E-commerce Customer Churn Prediction")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.info(
        """
        This application predicts customer churn probability 
        for e-commerce businesses.
        
        **Project Status:** 🚧 Under Development
        """
    )
    
    # API status check
    api_url = os.getenv("API_URL", "http://api:8000")
    
    try:
        response = requests.get(f"{api_url}/health", timeout=5)
        if response.status_code == 200:
            st.success("✅ API Connected")
        else:
            st.error("❌ API Error")
    except:
        st.warning("⚠️ API Unavailable")

# Main content
st.header("📊 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Dataset",
        value="Ready",
        delta="E-commerce Data"
    )

with col2:
    st.metric(
        label="Model Status",
        value="Training",
        delta="In Progress"
    )

with col3:
    st.metric(
        label="API Status",
        value="Active",
        delta="Running"
    )

st.markdown("---")

# Placeholder sections
st.header("🔮 Prediction")
st.info("Model training in progress. Prediction feature coming soon!")

st.header("📈 Visualizations")
st.info("Data analysis and visualizations will be available after EDA completion.")

st.markdown("---")
st.caption("Developed for AI & Machine Learning Final Project")