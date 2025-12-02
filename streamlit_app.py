import streamlit as st
import pandas as pd
import plotly

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

This is the first version of our interactive website, where we will:
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

    st.header("🔎 Region Explorer")
    st.markdown("Select a NUTS-2 region to explore its time-series indicators.")

    if df is None:
        st.warning("Please upload a dataset first in the Home page.")
    else:
        # ------------------------
        # Region Selector
        # ------------------------
        regions = sorted(df["geo"].dropna().unique())
        region = st.selectbox("Select a NUTS-2 region:", regions)

        df_region = df[df["geo"] == region].sort_values("year")

        st.subheader(f"📍 Region: **{region}**")
        st.write(df_region)

        st.divider()

        # ------------------------
        # Time-series plots
        # ------------------------

        numeric_columns = df_region.select_dtypes(include=["float64", "int64"]).columns

        available_vars = {
            "Tourism (Nights Spent)": "nights_spent",
            "GDP": "gdp",
            "Population": "pop",
            "Employment Rate": "employment",
            "Unemployment": "unemployment",
        }

        # Detect climate variables if present
        climate_vars = [col for col in numeric_columns if "temp" in col.lower() or "climate" in col.lower()]
        for c in climate_vars:
            available_vars[f"Climate: {c}"] = c

        st.header("📈 Time-Series Indicators")

        # Plot each available variable
        import plotly.express as px

        for label, col in available_vars.items():
            if col in df_region.columns:
                st.subheader(label)
                fig = px.line(
                    df_region,
                    x="year",
                    y=col,
                    markers=True,
                    title=f"{label} over time in {region}"
                )
                fig.update_layout(height=350)
                st.plotly_chart(fig, use_container_width=True)


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
