import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
import random

st.title("AI Mental Stress Detection Prototype")

st.write("Prototype system for predicting stress based on behavior.")

# -----------------------------
# User Inputs
# -----------------------------

typing_speed = st.slider("Typing Speed",20,100,50)
typing_errors = st.slider("Typing Errors",0,10,2)
screen_time = st.slider("Screen Time (hours)",0,10,3)

# -----------------------------
# Simple Training Data
# -----------------------------

X = np.array([
[65,1,2],
[40,8,6],
[55,3,3],
[35,10,7],
[70,1,1],
[50,4,4],
[30,9,8]
])

y = np.array([0,2,1,2,0,1,2])

model = RandomForestClassifier()
model.fit(X,y)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Stress"):

    prediction = model.predict([[typing_speed,typing_errors,screen_time]])

    if prediction == 0:
        st.success("Relaxed 😊")

    elif prediction == 1:
        st.warning("Moderate Stress 😐")

    else:
        st.error("High Stress 😟")

# -----------------------------
# Stress Trend Chart
# -----------------------------

st.header("Weekly Stress Trend")

data = pd.DataFrame({
"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
"Stress":[2,3,4,3,2,1,2]
})

fig, ax = plt.subplots()

ax.plot(data["Day"], data["Stress"], marker="o")

st.pyplot(fig)

# -----------------------------
# Wellness Suggestions
# -----------------------------

st.header("Wellness Suggestions")

if st.button("Get Suggestion"):

    tips = [
        "Take a short walk",
        "Drink water",
        "Practice deep breathing",
        "Listen to relaxing music",
        "Take a short break from screens"
    ]

    st.info(random.choice(tips))
