import streamlit as st
import pandas as pd
from app.valuation.valuation import calculate_track_value
from app.cleaning.cleaning import clean_incoming_data

# Load master catalog
master_path = "data/Master_Music_Catalog.csv"
df_master = pd.read_csv(master_path)

# Upload and clean new data
st.subheader("Upload New Data")
uploaded_file = st.file_uploader("Upload a CSV file for cleaning", type=["csv"])

if uploaded_file:
    # Save the uploaded file temporarily
    temp_file_path = f"data/uploads/{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Clean the uploaded data
    cleaned_data = clean_incoming_data(temp_file_path)
    st.write("Cleaned Data Preview:")
    st.dataframe(cleaned_data)

    # Validate against master catalog
    key_columns = ["artist_band", "broadcast_concert", "date", "song_title"]
    merged = pd.merge(cleaned_data, df_master, on=key_columns, how="left", indicator=True)
    duplicates = merged[merged["_merge"] == "both"]
    new_entries = merged[merged["_merge"] == "left_only"].drop(columns=["_merge"])

    st.write(f"Found {len(duplicates)} duplicates.")
    st.write(f"Adding {len(new_entries)} new entries to the master catalog.")

    if st.button("Add New Entries"):
        updated_master = pd.concat([df_master, new_entries]).drop_duplicates(subset=key_columns)
        updated_master.to_csv(master_path, index=False)
        st.success("New entries added to the master catalog!")

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

