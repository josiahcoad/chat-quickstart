from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

from agents.helloworld.tools import add, subtract

load_dotenv()

# for searching the web
# tavily_search = TavilySearchResults(max_results=5)

llm = init_chat_model(model="gpt-4o", temperature=0)

# Create the agent with custom system prompt
system_prompt = """
You talk like a pirate.
"""


graph = create_react_agent(
    llm,
    tools=[
        # tavily_search,
        add,
        subtract,
    ],
    prompt=system_prompt,
)

if __name__ == "__main__":
    response = graph.invoke({"message": "What is 10 + 10?"})
    response["messages"][-1].pretty_print()
