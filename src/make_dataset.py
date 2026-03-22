import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

"""
The data used in this exercise is derived from Capital Bikeshare 
"""


bike_data = pd.read_csv("../data/bike_data_raw.csv")
bike_data.info()


# Select relevant features
relevant_features = [
    "season",
    "mnth",
    "holiday",
    "weekday",
    "workingday",
    "weathersit",
    "temp",
    "atemp",
    "hum",
    "windspeed",
    "cnt",
]
bike_data = bike_data[relevant_features]

# Convert non-numerical columns to dtype category
categorical_features = [
    "season",
    "mnth",
    "holiday",
    "weekday",
    "workingday",
    "weathersit",
]
bike_data[categorical_features] = bike_data[categorical_features].astype("category")
bike_data.info()

# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------

bike_data.to_pickle("../data/bike_data_processed.pkl")
