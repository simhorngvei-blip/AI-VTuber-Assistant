import asyncio
from brain import AIBrain
from mouth import speak

async def main():
    # Initialize the Brain
    neuro = AIBrain()
    
    print("--- Neuro Clone Online (Type 'quit' to exit) ---")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["quit", "exit"]:
            break
            
        # 1. Think
        reply = neuro.think(user_input)
        
        # 2. Print
        print(f"Neuro: {reply}")
        
        # 3. Speak
        await speak(reply)

if __name__ == "__main__":
    asyncio.run(main())