import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import random

st.set_page_config(page_title="Mental Wellness AI", layout="wide")

st.title("🧠 Mental Wellness AI Dashboard")

st.write("Monitor stress levels and receive AI wellness suggestions.")

# ----------------------------
# Behavior Stress Prediction
# ----------------------------

st.header("Behavior Stress Prediction")

typing_speed = st.slider("Typing Speed",20,100,50)
typing_errors = st.slider("Typing Errors",0,10,2)
screen_time = st.slider("Screen Time (hours)",0,10,3)

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

if st.button("Predict Stress Level"):

    prediction = model.predict([[typing_speed,typing_errors,screen_time]])

    if prediction == 0:
        st.success("Relaxed 😊")
    elif prediction == 1:
        st.warning("Moderate Stress 😐")
    else:
        st.error("High Stress 😟")

# ----------------------------
# Mood Tracker
# ----------------------------

st.header("Daily Mood Tracker")

mood = st.selectbox(
"How do you feel today?",
["Happy","Calm","Neutral","Tired","Stressed"]
)

if st.button("Save Mood"):

    st.success(f"Mood recorded: {mood}")

# ----------------------------
# Stress Trend Dashboard
# ----------------------------

st.header("Weekly Stress Trend")

data = pd.DataFrame({
"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
"Stress":[2,3,4,3,2,1,2]
})

fig, ax = plt.subplots()

ax.plot(data["Day"], data["Stress"], marker="o")

ax.set_xlabel("Day")
ax.set_ylabel("Stress Level")

st.pyplot(fig)

# ----------------------------
# AI Wellness Suggestions
# ----------------------------

st.header("AI Wellness Suggestions")

if st.button("Get Suggestion"):

    tips = [
        "Take a short walk",
        "Practice deep breathing",
        "Drink water",
        "Take a 10 minute break",
        "Listen to relaxing music",
        "Stretch your body"
    ]

    st.info(random.choice(tips))

