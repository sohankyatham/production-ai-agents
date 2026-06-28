# Production AI Agents
This repository is a comprehensive guide to building production-ready AI agents in Python using the AgentSpan framework, covering essential production features like RAG, guardrails, and multi-agent orchestration. 

Three Agents:
1. Persistent Context Agent
2. Support Agent
3. Multi-Agent Orchestration

> This repository contains my implementation of the agents built during the tutorial course: [Tech With Tim 'Build 3 PRODUCTION AI Agents in Python - Full Course (Agentspan)' course](youtube.com/watch?v=zFw19qGAeGo)

## Purpose
I created this repository to practice building production-ready AI agents using the AgentSpan framework. 

Learned:
- Conversational agents with memory.
- RAG-based support agents with human-in-the-loop approval.
- Multi-agent orchestration strategies.
- Implementing input guardrails and structured outputs.

Where in-process agents break:
- Process crashes mid-run
- Human-in-the-loop breaks
- No visibility
- Scaling = reinventing 

7 Things for AI Agents to be Production Ready:
- Durability
- Retries
- Human-in-the-loop
- Observability
- Long-running tasks
- Scale
- Testing

Architecture:
- Worker
- Server
- LLM


## Setup
[Agentspan Documentation](https://agentspan.ai/docs/)

`pip install agentspan`

Verify setup: `agentspan doctor`

Java 21: Required to run the local AgentSpan server
API Keys: You will need a valid LLM API key (e.g., OpenAI, Gemini, Anthropic) to execute the agent logic

- Create a .env file to manage credentials