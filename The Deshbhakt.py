import numpy as np
import pandas as pd
import streamlit as st     
import pickle, io 
import warnings
warnings.filterwarnings("ignore")

# Load the trained model

model = pickle.load(open("The Deshbhakt.pkl", "rb"))

st.title("YouTube Video Popularity Predictor")

# Feature inputs
col1, col2 = st.columns(2)
with col1:
    likes = st.number_input("Likes", min_value=0, help="Enter total number of likes")
    comments = st.number_input("Comments", min_value=0, help="Total number of comments")
    views = st.number_input("Views", min_value=0, help="Number of views in the video")


with col2:
    is_short = st.checkbox("Short Video (<60s)", help="Check if the video is shorter than 60 seconds")
    publish_day = st.slider("Publish Day", 1, 31, help="Day of month published")
    publish_month = st.slider("Publish Month", 1, 12, help="Month published (1–12)")


input_data = pd.DataFrame([[likes, comments, views,
                            is_short, publish_day, publish_month]],
                            columns=["likes","comments","views","is_short","publish_day","publish_month"])

prediction = model.predict(input_data)[0]
if prediction == 1:
    st.success("Prediction: **Popular** 🎉", icon="✅")
else:

    st.info("Prediction: **Not Popular** 😐", icon="ℹ️")
