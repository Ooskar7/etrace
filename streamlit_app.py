import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# E-TRACE: European Tourism Regional Analysis & Climate Effects
# Basic Streamlit Frontend Starter Template
# ---------------------------------------------------------

# Page configuration
st.set_page_config(
    page_title="E-TRACE Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.title("🌍 E-TRACE Dashboard")
st.markdown("""
Welcome to **E-TRACE** — European Tourism Regional Analysis & Climate Effects.

This is the first version of your frontend, where we will:
- Upload and explore the dataset
- Visualize trends (tourism activity, population, GDP, employment, climate variables…)
- Build predictive insights
- Interactively compare NUTS-2 regions

This page is just a starting point — we will expand it into multiple tabs and visualizations.
""")

st.divider()

# ---------------------------------------------------------
# Dataset Loader Section
# ---------------------------------------------------------
st.header("📁 Load Your Processed Dataset")

uploaded_file = st.file_uploader(
    "Upload the merged dataset (CSV/Parquet)",
    type=["csv", "parquet"]
)

df = None

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_parquet(uploaded_file)

    st.success("Dataset loaded successfully!")
    st.write("### Preview of the data:")
    st.dataframe(df.head())

    st.write("### Dataset statistics:")
    st.write(df.describe(include="all"))


# ---------------------------------------------------------
# Sidebar Navigation (for future pages)
# ---------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Exploration", "Models"])

if page == "Exploration":
    st.header("🔎 Data Exploration")
    st.write("Coming soon: graphs, filters, regional comparisons…")

elif page == "Models":
    st.header("🤖 Predictive Models")
    st.write("Coming soon: model training, forecasting, climate-tourism interactions…")


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.write(
    "E-TRACE • European Tourism Regional Analysis & Climate Effects • Built with ❤️ using Streamlit"
)
