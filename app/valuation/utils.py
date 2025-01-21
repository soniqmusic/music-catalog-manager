# utils.py - Supporting functions for valuation

def classify_rarity(track_metadata):
    """
    Classify rarity based on track metadata.

    Parameters:
        track_metadata (dict): Dictionary containing track metadata.

    Returns:
        str: Rarity classification ('low', 'medium', 'high').
    """
    if track_metadata.get("broadcast_age", 0) > 40:  # 40 years or older
        return "high"
    elif track_metadata.get("broadcast_age", 0) > 20:
        return "medium"
    else:
        return "low"
