from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from brain import AIBrain
from mouth import generate_audio # We reuse your existing mouth code!

app = FastAPI()
neuro = AIBrain()

class ChatRequest(BaseModel):
    text: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    print(f"Unity sent: {request.text}")
    
    # 1. Get Text Reply
    reply_text = neuro.think(request.text)
    
    # 2. Generate Audio File
    # We await this because generating audio takes a second
    audio_filename = "reply.mp3"
    await generate_audio(reply_text)
    
    # 3. Return BOTH text and the audio file path
    # We return a JSON that tells Unity where to download the audio
    return {
        "reply": reply_text,
        "audio_url": "http://127.0.0.1:8000/get_audio"
    }

@app.get("/get_audio")
def get_audio():
    """Unity calls this to download the MP3"""
    audio_file = "speech.mp3" # This matches what mouth.py outputs
    if os.path.exists(audio_file):
        return FileResponse(audio_file, media_type="audio/mpeg")
    raise HTTPException(status_code=404, detail="Audio not found")