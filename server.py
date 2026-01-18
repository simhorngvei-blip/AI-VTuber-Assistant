from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel
import shutil
import os

# Import your existing organs
from brain import AIBrain
from ears import AIEars
# Note: We don't import 'mouth' yet because the server shouldn't speak. 
# The server should send audio FILES to the client (your phone).

app = FastAPI()
neuro = AIBrain()

# Define the data format for text input
class ChatRequest(BaseModel):
    text: str

@app.get("/")
def health_check():
    """Just to check if the server is alive"""
    return {"status": "Neuro is Online", "version": "1.0.0"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    """
    Mobile App sends TEXT -> Server returns TEXT
    """
    print(f"Client said: {request.text}")
    reply = neuro.think(request.text)
    return {"reply": reply}

@app.post("/hear")
async def hear_endpoint(file: UploadFile = File(...)):
    """
    Mobile App sends AUDIO FILE -> Server listens -> Server returns TEXT reply
    """
    # 1. Save the uploaded file temporarily
    temp_filename = "temp_input.wav"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. Use existing 'ears' logic (You might need to tweak ears.py to accept files)
    # For now, let's just acknowledge receipt
    return {"status": "Audio received", "filename": file.filename}

# To run this: uvicorn server:app --reload