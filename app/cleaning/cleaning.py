import pandas as pd
import streamlit as st

def clean_incoming_data(file_path):
    """
    Clean and standardize incoming data for the master catalog.

    Parameters:
        file_path (str): Path to the incoming CSV file.

    Returns:
        pd.DataFrame: Cleaned and standardized DataFrame.
    """
    df = pd.read_csv(file_path)

    # Standardize column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r"[()]", "", regex=True)
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.lower()

    # Fill missing values
    df["artist_band"] = df.get("artist_band", "").fillna("Unknown Artist")
    df["broadcast_concert"] = df.get("broadcast_concert", "").fillna("Unknown Broadcast")
    df["date"] = df.get("date", "").fillna("Unknown Date")
    df["track_order"] = pd.to_numeric(df.get("track_order", 0), errors="coerce").fillna(0).astype(int)
    df["song_title"] = df.get("song_title", "").fillna("Unknown Song")

    # Drop invalid rows (e.g., missing essential info)
    df = df[df["song_title"] != ""]
    df = df[df["artist_band"] != ""]

    return df
