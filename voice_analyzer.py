import librosa
import numpy as np

def analyze_voice(audio_file):

    y, sr = librosa.load(audio_file)

    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    score = np.mean(mfcc)

    if score > -200:
        return "Possible Stress"
    else:
        return "Calm Voice"
