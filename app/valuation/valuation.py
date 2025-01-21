# valuation.py - Logic for track valuation

def calculate_track_value(streams, rarity="medium"):
    """
    Calculate the estimated value of a track based on streams and rarity.

    Parameters:
        streams (int): Number of streams for the track.
        rarity (str): Rarity level of the track. Options: 'low', 'medium', 'high'.

    Returns:
        float: The estimated value of the track in USD.
    """
    base_value = 100  # Base value in USD
    rarity_multiplier = {"low": 1, "medium": 1.5, "high": 2}.get(rarity, 1)
    revenue = streams * 0.01  # Revenue generated from streams ($0.01 per stream)

    return base_value * rarity_multiplier + revenue
