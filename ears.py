import whisper
import sounddevice as sd
import numpy as np
import os
import colorama

# Configuration
# "base" is a good balance of speed and accuracy. Use "tiny" if it's too slow.
MODEL_TYPE = "base" 

class AIEars:
    def __init__(self):
        print(colorama.Fore.YELLOW + "Loading Ear Model (Whisper)..." + colorama.Style.RESET_ALL)
        self.model = whisper.load_model(MODEL_TYPE)

    def listen(self, duration=5):
        print(colorama.Fore.GREEN + f"Listening ({duration}s)..." + colorama.Style.RESET_ALL)
        
        # 1. Record Audio
        audio = sd.rec(int(duration * 16000), samplerate=16000, channels=1, dtype='float32')
        sd.wait() # Wait for recording to finish
        
        # 2. Transcribe
        print("Transcribing...")
        # Whisper expects a flattened array
        result = self.model.transcribe(audio.flatten(), fp16=False)
        text = result["text"].strip()
        
        print(f"You said: '{text}'")
        return text

# Test Block
if __name__ == "__main__":
    ears = AIEars()
    ears.listen()