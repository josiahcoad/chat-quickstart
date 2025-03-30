
# Multi-agent systems
### Handle more complex tasks

My math teacher told me that it gets harder the more you learn because you have more tools to choose from. That's exactly what happens with agents.
As your list of tools grows, the LLM might start having trouble knowing which one to use.
The way this is solved is via multi-agent systems. There are two main types:
- **Hierarchical agents**: where one agent is responsible for deciding which tool to use
  - Supervisor: https://github.com/langchain-ai/langgraph-supervisor-py
- **Coordinated agents**: where one agent is responsible for coordinating the actions of multiple agents
  - Swarm: https://github.com/langchain-ai/langgraph-swarm-py

* There is another motivating factor for using multi-agent systems... our system prompt is getting too long. We use the system prompt to guide the agent's behavior. If a single agent is doing too much, the system prompt will become too long.
