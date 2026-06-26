# RAG-based agent, Guardrails & HIML
import logging

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from agentspan.agents import (
    Agent,
    AgentRuntime,
    ConversationMemory,
    EventType,
    Guardrail,
    GuardrailResult,
    OnFail,
    Position,
    guardrail,
    start,
    tool,
)

load_dotenv(override=True)
logging.basicConfig(level=logging.WARNING, force=True)
logging.disable(logging.INFO)

MOCK_DB = {
    "orders": {"A100": {"status": "delivered", "total": 49.99}},
    "accounts": {"tim@example.com": {"status": "active", "tier": "pro"}},
}

DOCS = {
    "refund policy": "Refunds are processed within 5 business days.",
    "shipping": "Standard shipping takes 3 to 7 business days.",
    "account": "Pro accounts include priority support.",
}

# Pydantic object
class SupportResponse(BaseModel):
    stage: str = Field(description="Stage like answered, refunded, or rejected")
    successful: bool
    message: str

@tool
def search_knowledge_base(query: str) -> str:
    """search support doc"""
    # Quick keyword search
    for title, body in DOCS.items():
        if title in query.lower():
            return body
    return "No matching support articles found."

@tool
def lookup_order(order_id: str) -> dict:
    """lookup order in database by ID"""
    return MOCK_DB["orders"].get(order_id, {"error": "order not found"})

support_agent = Agent(
    name="support_agent",
    model="google_gemini/gemini-2.5-flash",
    instructions=(
        "You are a customer support agent. Use the knowledge base first. "
        "If the customer wants a refund: when you know the order ID, call "
        "lookup_order to get the amount. Before calling process_refund, "
        "write a short plain-English sentence describing exactly what refund "
        "you are about to issue, for example: 'I am going to refund $49.99 "
        "for order A100.' Then call process_refund. The tool will pause for "
        "human approval automatically. If the order ID is missing, ask the "
        "customer for it. Always populate the message field with a clear reply."
    ),
    output_type=SupportResponse,
    tools=[search_knowledge_base, lookup_order],
    memory=ConversationMemory(max_messages=50),
    max_turns=10,
)

def run_interactive(prompt: str) -> None:
    with AgentRuntime() as runtime:
        handle = start(support_agent, prompt, runtime=runtime)
        stream = handle.stream()

        order_id, amount = None, None
        for event in stream:
            pass

        result = stream.get_result()
        output = result

        print(f"\n{output}\n")


if __name__ == "__main__":
    print("Support bot starting...")
    while True:
        prompt = input("You: ").strip()
        if prompt.lower() == "q":
            break
        if not prompt:
            continue
        run_interactive(prompt)