import streamlit as st
import pandas as pd
from app.valuation.valuation import calculate_track_value

# Load data
master_path = "data/Master_Music_Catalog.csv"
df = pd.read_csv(master_path)

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

