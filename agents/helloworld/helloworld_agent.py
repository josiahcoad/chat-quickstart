import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

from agents.helloworld.tools import add, subtract

load_dotenv()

if os.getenv("TAVILY_API_KEY"):
    tavily_search = TavilySearchResults(max_results=5)
else:
    tavily_search = None

llm = init_chat_model(model="gpt-4o", temperature=0)

# Create the agent with custom system prompt
system_prompt = "Talk like a pirate."


graph = create_react_agent(
    llm,
    tools=[
        add,
        subtract,
        tavily_search,
    ],
    prompt=system_prompt,
)

if __name__ == "__main__":
    response = graph.invoke({"messages": ["What is 2+2?"]})
    print(response)
