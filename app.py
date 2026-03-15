import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
from fer import FER
import av

st.title("AI Stress Detection using Webcam")

detector = FER()

def video_frame_callback(frame):

    img = frame.to_ndarray(format="bgr24")

    emotions = detector.detect_emotions(img)

    if emotions:

        emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)

        cv2.putText(
            img,
            emotion,
            (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="stress-detect",
    video_frame_callback=video_frame_callback
)
       
