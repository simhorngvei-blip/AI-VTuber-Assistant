import edge_tts
import pygame
import asyncio
import os

# Configuration
VOICE = "en-IE-EmilyNeural" # A cute female voice
OUTPUT_FILE = "speech.mp3"

async def generate_audio(text):
    """Converts text to an MP3 file"""
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio():
    """Plays the generated MP3 file"""
    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()
    
    # Wait until audio finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.quit()
    # Clean up file
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

async def speak(text):
    print(f"Speaking: {text}")
    await generate_audio(text)
    play_audio()