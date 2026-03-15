from fer import FER

detector = FER()

def detect_emotion(image):

    emotions = detector.detect_emotions(image)

    if emotions:
        emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)
        return emotion
    else:
        return "No face detected"
