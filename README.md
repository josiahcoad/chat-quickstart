# Getting Started with Chat Agents

## Quick Start
```bash
make setup && source .venv/bin/activate # setup venv
cp .env-example .env # then edit `.env`
make test # run the agent with a single input to make sure it works
make dev # run the dev server for the chat UI
```

This repository demonstrates how to create a chat bot (think chatgpt) using LangGraph.

It uses a "ReAct agent" (short for Reasoning and Action agent) which is basically just an LLM that can call tools.

While simple, it is incredibly powerful and can be extended to do more complex tasks.

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
- You can deploy the agent using docker and ec2/etc
- You can also do a managed deployment using https://langchain-ai.github.io/langgraph/cloud/deployment/cloud
- Deploy the frontend using...

### 7. Add storage retrieval (R.A.G.)
- Retrieving and storing documents can be thought of as another tool
- Consider adding repositories to the agent as tools which tell the agent where to look for particular information

### 8. Add (long-term) memory
- https://youtu.be/-xkduCeudgY?si=qFi2h3BMj7sBqMrm
- "short term memory" is just the conversation history so that the LLM knows what has been said so far
- "long term memory" is just a key value store that the LLM can use to store information
  - it decided when to store info and then the entire store is included in every system prompt of the chat
  - this helps is remember and update preferences of the user

### 9. Add a GUI to your chat app
- https://youtu.be/sCqN01R8nIQ?si=AXGrNoyt0ZtuqegW


### 10. Check out MCP servers
Tools are great but they are a python function...
MCP servers are just an abstraction on top of tools that give a language-agnostic way to communicate with them over stdin/stdout
And a way to group tools together into packages.

- this is pretty badass https://github.com/snaggle-ai/openapi-mcp-server
- and it might help to find out how tou can make an MCP server from scratch: https://youtu.be/CDjjaTALI68?si=rDPJeBcbX0Y-yUFc
- there are a ton available
  - like here: https://github.com/modelcontextprotocol/servers
  - https://github.com/punkpeye/awesome-mcp-servers
  - and a fully hosted platform of them here: https://composio.dev/



## Extra Helpful Links

**General langchain docs:**
- https://python.langchain.com/api_reference


### Interacting with memory
- https://github.com/langchain-ai/langgraph-memory


### Interacting with storage
**"Document" Loaders**
- Documents are anything that have "page_content" and "metadata"
- https://python.langchain.com/docs/integrations/document_loaders/