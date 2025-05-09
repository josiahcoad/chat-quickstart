# Getting Started with Chat Agents

## Quick Start
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh # install uv
brew install make # install make
```

```bash
make setup-env && source .venv/bin/activate # setup venv
cp .env-example .env # then edit `.env`
make demo # run the agent with a single input to make sure it works
make dev # run the dev server for the chat UI
```

This repository demonstrates how to create a chat bot (think chatgpt) using LangGraph. But extended with tools, memory, and a GUI.

It uses a "ReAct agent" (short for Reasoning and Action agent) which is basically just an LLM that can call tools.

While simple, it is incredibly powerful and can be extended to do many complex tasks.


### If you prefer using docker
```bash
cp .env-example .env # then edit `.env`
docker compose up
```

The navigate to https://smith.langchain.com/studio/thread?baseUrl=http://127.0.0.1:2024

## Dev Notes
- we use uv (rust based package manager) for super fast installs
- we use ruff for linting and formatting

### Glossary
#### The LangX Stack
- Lansmith: a platform for tracing and monitoring your LLM apps
- LangChain: a library for building LLM based apps (chains are sequences of LLM calls basically)
- LangGraph: a library for building stateful, multi-step LLM workflows (built on top of LangChain but extends it with graphs)
- LangGraph Studio: a UI for viewing and interacting with LangGraph graphs

## Path to get started
### 1. Create a langsmith account and add your API key to the .env file
   - https://smith.langchain.com/

### 2. Create an agent (an agent is a particular type of graph)
- this has been done in the agent/assistant.py file

### 3. Serve that agent
- Run `make dev`
- This should open the graph here: https://smith.langchain.com/studio

### 4. Connect to that agent via the UI
- Navigate to: https://agentchat.vercel.app/
  - Use the defaults: agent
- btw its open source so you can run/deploy it locally too:
- https://github.com/langchain-ai/agent-chat-ui

### 5. Add a tool
- A tool has already been added in the agent/tools/arithmetic.py file
- Anything that can be a python function can be a tool
- lots of prebuilt tools from langchain: https://python.langchain.com/docs/integrations/tools/

### 6. Deploy your agent on the cloud
- Langgraph offers a managed deployment (Langgraph Cloud/Platform)
  - go to https://smith.langchain.com/ and click the langgraph platform tab
  - click new deployment in top right
  - fork this repo into your own github account
  - point the deployment to your fork
  - click deploy
- Deploy the frontend using... (TODO)
- You can also deploy the langgraph server yourself
  - using docker and ec2
    - https://langchain-ai.github.io/langgraph/cloud/reference/cli/#up
    - "Requires a license key for production use." (TODO: need to look into this)
    - You'll need to manage thread/chat/"short-term" memory yourself
    - If using long-term memory, you'll need to manage that yourself too
  - invoking the graph manually behind your own api
    - check out langserve for that (although it has been soft deprecated in favor of langgraph platform)

### Build more complex agents...
- An agent with memory: [./agents/memory/README.md](./agents/memory/README.md)
- An agent with storage: [./agents/storage/README.md](./agents/storage/README.md)
- An agent with multi-step conversations: [./agents/multiagent/README.md](./agents/multiagent/README.md)


## Extra Helpful Links

### General langchain docs
- https://python.langchain.com/api_reference
- https://langchain-ai.github.io/langgraph/cloud/deployment/cloud

### Check out MCP servers
Tools are great but they are a python function...
MCP servers are just an abstraction on top of tools that give a language-agnostic way to communicate with them over stdin/stdout
And a way to group tools together into packages.

- this is pretty badass https://github.com/snaggle-ai/openapi-mcp-server
- and it might help to find out how tou can make an MCP server from scratch: https://youtu.be/CDjjaTALI68?si=rDPJeBcbX0Y-yUFc
- there are a ton available
  - like here: https://github.com/modelcontextprotocol/servers
  - https://github.com/punkpeye/awesome-mcp-servers
  - and a fully hosted platform of them here: https://composio.dev/

### Add a GUI to your chat app
- https://youtu.be/sCqN01R8nIQ?si=AXGrNoyt0ZtuqegW
- This is not yet possible in python yet but hopefully soon!
