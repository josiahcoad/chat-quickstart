# Getting Started with Chat Agents

## Quick Start
```bash
make setup
make demo
make dev
```

This repository demonstrates how to create chat agents using LangGraph.

## Dev Notes
- we use uv (rust based package manager) for super fast installs

The LangX Glossary
- Lansmith: a paid service for tracing and monitoring your LLM apps
- LangChain: a library for building LLM based apps (chains are sequences of LLM calls basically)
- LangGraph: a library for building stateful, multi-step LLM workflows (built on top of LangChain but extends it with graphs)
- LangGraph Studio: a UI for viewing and interacting with LangGraph graphs

## Path to get started
### 1. Create a langsmith account and add your API key to the .env file (it's free)
   - https://smith.langchain.com/

### 2. Create an agent (an agent is a particular type of graph)
- this has been done in the agent/assistant.py file

### 3. Serve that agent
- Run `langgraph dev`
- This should open the graph here: https://smith.langchain.com/studio

### 4. Connect to that agent via the UI
- Navigate to: https://agentchat.vercel.app/
  - Use the defaults: agent
- btw its open source so you can run/deploy it locally too:
- https://github.com/langchain-ai/agent-chat-ui

### 5. Add a tool

### 6. Deploy your agent on the cloud

### 7. Discover the universe of tools available

### 8. Check our MCP servers
Tools are great but they were a python function... Also you had to define each out
MCP servers are just an abstraction on top of tools that give a language agnostic way to communicate with them over stdin/stdout

- this is pretty badass https://github.com/snaggle-ai/openapi-mcp-server

### 9. Check out how to add GUI to your assistant
- https://youtu.be/sCqN01R8nIQ?si=AXGrNoyt0ZtuqegW


## Extra Helpful Links

**General langchaindocs:**
- https://python.langchain.com/api_reference


### Interacting with memory
- https://github.com/langchain-ai/langgraph-memory


### Interacting with storage
**"Document" Loaders**
- Documents are anything that have "page_content" and "metadata"
- https://python.langchain.com/docs/integrations/document_loaders/