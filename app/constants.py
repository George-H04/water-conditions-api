"""
A file containing all constants and conversion factors. Required as some
APIs return data with magic number identifiers, instead of descriptive names
"""

USGS_IDS = {
    "00010": "water temperature",
    "00011": "water temperature",
    "00045": "precipitation",
    "00060": "flow rate",
    "00065": "water level",
}

UNITS = {
    "00010": "°C",
    "00011": "°F",
    "00045": "Inches",
    "00060": "CFS",
    "00065": "Feet",
}
