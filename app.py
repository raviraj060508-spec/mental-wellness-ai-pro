import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Mental Wellness AI")

st.write("Basic stress prediction demo.")

typing_speed = st.slider("Typing Speed",20,100,50)
typing_errors = st.slider("Typing Errors",0,10,2)
screen_time = st.slider("Screen Time (hours)",0,10,3)

X = np.array([
[65,1,2],
[40,8,6],
[55,3,3],
[35,10,7],
[70,1,1]
])

y = np.array([0,2,1,2,0])

model = RandomForestClassifier()
model.fit(X,y)

if st.button("Predict Stress"):
    
    prediction = model.predict([[typing_speed,typing_errors,screen_time]])

    if prediction == 0:
        st.success("Relaxed")
    elif prediction == 1:
        st.warning("Moderate Stress")
    else:
        st.error("High Stress")




