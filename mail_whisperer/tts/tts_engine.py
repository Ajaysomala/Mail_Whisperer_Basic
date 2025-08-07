# tts/tts_engine.py

from gtts import gTTS
import os
from datetime import datetime

def text_to_speech(text, filename=None, lang='en'):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"summary_{timestamp}.mp3"
    filepath = os.path.join("static", "audio_output", filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(filepath)
    return filepath
