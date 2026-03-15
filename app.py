import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av

st.title("Webcam Stress Detection")

def video_frame_callback(frame):

    img = frame.to_ndarray(format="bgr24")

    cv2.putText(
        img,
        "Stress Monitoring Active",
        (30,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="webcam",
    video_frame_callback=video_frame_callback
)
         
