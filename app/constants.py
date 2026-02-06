"""
A file containing all constants and conversion factors. Required as some
APIs return data with magic number identifiers, instead of descriptive names
"""

USGS_IDS = {
    "00010": "Water temperature",
    "00011": "Water temperature",
    "00045": "Precipitation",
    "00060": "Flow rate",
    "00065": "Water level",
}

UNITS = {
    "00010": "°C",
    "00011": "°F",
    "00045": "Inches",
    "00060": "CFS",
    "00065": "Feet",
}
