# Hello World Agent

This is about as simple as it gets with LangGraph.

Here you create an ReAct agent that uses a couple math tools.

## Running the agent

```bash
python agents/helloworld/assistant.py
```

### Adding internet search to the tool

there is commented out code for `tavily_search` tool. Just add your API key to the `.env` file and uncomment the code.

