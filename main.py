import asyncio
from brain import AIBrain
from mouth import speak
from ears import AIEars

async def main():
    # 1. Initialize all organs
    print("--- Booting up Neuro ---")
    neuro_brain = AIBrain()
    neuro_ears = AIEars()
    
    print("--- Neuro is Online (Say 'Goodbye' to exit) ---")
    
    while True:
        # A. LISTEN (Microphone)
        # We listen for 5 seconds. You can change this duration.
        user_input = neuro_ears.listen(duration=5)
        
        # Skip empty silence
        if len(user_input) < 2:
            continue
            
        if "goodbye" in user_input.lower():
            break
            
        # B. THINK (Brain)
        reply = neuro_brain.think(user_input)
        
        # C. SPEAK (Mouth)
        await speak(reply)

if __name__ == "__main__":
    asyncio.run(main())