import logging
from datetime import datetime

from dotenv import load_dotenv

from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool


load_dotenv()
logging.basicConfig(level=logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("conductor").setLevel(logging.WARNING)

assistant = Agent(
    name="personal_assistant",
    model="google_gemini/gemini-2.5-flash",
    instructions=(
        "You are a concise personal assistant. Use tools when they help"
        "and remember useful user details across turns"
    ),
    tools=[]
)

if __name__ == "__main__":
    print("Starting agent...")

    with AgentRuntime() as runtime:
        while True:
            prompt = input("You: ").strip()
            if prompt.lower() == "q":
                break
            if not prompt:
                continue

            result = run(assistant, prompt, runtime=runtime)
            print(f"Assistant: {result}")