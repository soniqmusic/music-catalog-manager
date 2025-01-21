import streamlit as st
import pandas as pd

# Load data
master_path = "/content/Master_Music_Catalog.csv"
df = pd.read_csv(master_path)

# Simulated Metrics
total_tracks = len(df)
total_streams = df["Streams"].sum() if "Streams" in df.columns else 0
total_revenue = total_streams * 0.01  # Example $0.01 per stream

# Dashboard
st.title("Iconic Music Archive Dashboard")
st.subheader("Overview")

# Display key metrics
st.metric("Total Tracks", total_tracks)
st.metric("Total Streams", f"{total_streams:,}")
st.metric("Total Revenue (USD)", f"${total_revenue:,.2f}")
