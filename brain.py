import ollama
from colorama import Fore, Style

# Configuration
MODEL_NAME = "llama3" 

class AIBrain:
    def __init__(self):
        self.history = [
            {"role": "system", "content": "You are a VTuber AI Assistant. You are helpful but slightly sassy. Keep answers under 2 sentences."}
        ]

    def think(self, user_input):
        """Sends text to Llama 3 and gets a response"""
        
        # Add user input to memory
        self.history.append({"role": "user", "content": user_input})
        
        print(Fore.CYAN + "Thinking..." + Style.RESET_ALL)
        
        # Call the API
        response = ollama.chat(model=MODEL_NAME, messages=self.history)
        reply = response['message']['content']
        
        # Add reply to memory
        self.history.append({"role": "assistant", "content": reply})
        
        return reply

# Testing block (Only runs if you run this file directly)
if __name__ == "__main__":
    bot = AIBrain()
    print(bot.think("Hello! Who are you?"))