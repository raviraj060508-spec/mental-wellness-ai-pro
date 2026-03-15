import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import random
from fer import FER
import cv2

st.set_page_config(page_title="Mental Wellness AI", layout="wide")

st.title("🧠 Mental Wellness AI System")

# ----------------------------
# AI Stress Prediction
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

if st.button("Predict Stress"):

    prediction = model.predict([[typing_speed,typing_errors,screen_time]])

    if prediction == 0:
        st.success("Relaxed 😊")
    elif prediction == 1:
        st.warning("Moderate Stress 😐")
    else:
        st.error("High Stress 😟")

# ----------------------------
# Face Emotion Detection
# ----------------------------

st.header("Face Emotion Detection")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

emotion_detector = FER()

while run:

    ret, frame = camera.read()

    if not ret:
        st.write("Camera not detected")
        break

    emotions = emotion_detector.detect_emotions(frame)

    if emotions:

        emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)

        cv2.putText(frame, emotion, (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,255,0),2)

    FRAME_WINDOW.image(frame)

camera.release()

# ----------------------------
# Stress Trend Chart
# ----------------------------

st.header("Weekly Stress Trend")

data = pd.DataFrame({
"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
"Stress":[2,3,4,3,2,1,2]
})

fig, ax = plt.subplots()

ax.plot(data["Day"], data["Stress"], marker="o")

st.pyplot(fig)

# ----------------------------
# Wellness Suggestions
# ----------------------------

st.header("AI Wellness Suggestions")

if st.button("Get Tip"):

    tips = [
        "Take a short walk",
        "Practice deep breathing",
        "Drink water",
        "Take a break from screens",
        "Listen to relaxing music",
        "Stretch your body"
    ]

    st.info(random.choice(tips))
       
