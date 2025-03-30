# Adding memory
### "long-term" memory can help the LLM remember and update preferences of the user

- See explanation here: https://youtu.be/-xkduCeudgY?si=qFi2h3BMj7sBqMrm
- "short term memory" is just the conversation history so that the LLM knows what has been said so far
- "long term memory" is just a key value store that the LLM can use to store information
  - the LLM decides when to store info (via a tool call)
  - and the entire store is included in every subsequent system prompt of the chat
  - this helps is remember and update preferences of the user
  - but be careful about this memory getting too big
    - You don't want to store big documents this way. That's where storage comes in...
- to interact with it, go to https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=memory_agent


* Btw, if you deploy your agent on langgraph platform, there is build in memory persistence. To enable, just add a third argument to the nodes of the graph. For example:

```python
def my_node(state: dict, config: RunnableConfig, store: BaseStore) -> dict:
    return state

graph = Workflow()
graph.add_entry_point(my_node)
```



## More on memory
- Example repo using memory: https://github.com/langchain-ai/langgraph-memory
