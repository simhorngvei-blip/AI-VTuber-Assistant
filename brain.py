import requests
import json
from colorama import Fore, Style

# Configuration
MODEL_NAME = "llama3"
OLLAMA_URL = "http://localhost:11434/api/chat"

class AIBrain:
    def __init__(self):
        self.history = [
            {"role": "system", "content": "You are a VTuber AI. Keep answers short and sassy."}
        ]

    def think(self, user_input):
        # 1. Add user input to memory
        self.history.append({"role": "user", "content": user_input})
        
        print(Fore.CYAN + "Thinking..." + Style.RESET_ALL)
        
        # 2. Prepare the payload (The data packet)
        payload = {
            "model": MODEL_NAME,
            "messages": self.history,
            "stream": False, # Wait for full answer (easier for beginners)
            "options": {
                "num_ctx": 2048 # LIMIT MEMORY to prevent CUDA crashes
            }
        }
        
        try:
            # 3. Send the request (Directly to the engine)
            response = requests.post(OLLAMA_URL, json=payload)
            response.raise_for_status() # Check for HTTP errors
            
            # 4. Parse the answer
            data = response.json()
            reply = data['message']['content']
            
            # 5. Add reply to memory
            self.history.append({"role": "assistant", "content": reply})
            return reply

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error talking to Ollama: {e}" + Style.RESET_ALL)
            return "My brain is disconnected."

# Test block
if __name__ == "__main__":
    bot = AIBrain()
    print(bot.think("Hello!"))