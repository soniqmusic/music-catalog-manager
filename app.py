import streamlit as st
import pandas as pd
from app.valuation.valuation import calculate_track_value

# Load data
master_path = "data/Master_Music_Catalog.csv"
df = pd.read_csv(master_path)

# App configuration
st.set_page_config(page_title="Iconic Music Archive", layout="wide")

# Sidebar
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("Iconic Music Archive")
st.sidebar.markdown("Preserve the legacy of iconic performances.")

# Dashboard Metrics
st.title("Music Archive Dashboard")
st.markdown("### Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Tracks", len(df))
col2.metric("Total Streams", df["Streams"].sum() if "Streams" in df.columns else 0)
col3.metric("Total Revenue (USD)", f"${(df['Streams'].sum() * 0.01):,.2f}" if "Streams" in df.columns else "$0.00")
# Simulated Streams
if "Streams" not in df.columns:
    df["Streams"] = [5000, 10000, 20000]  # Example streams for testing

# Add Valuation Column
df["Estimated Value (USD)"] = df.apply(
    lambda row: calculate_track_value(row["Streams"], rarity="medium"),
    axis=1
)

# Streamlit App
st.title("Iconic Music Archive Dashboard")

# Display DataFrame with Valuation
st.subheader("Track Valuation")
st.dataframe(df[["Artist/Band", "Song Title", "Streams", "Estimated Value (USD)"]])

