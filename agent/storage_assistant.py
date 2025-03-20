import json

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from agent.tools.storage import add_to_storage, search_storage

load_dotenv()

llm = init_chat_model(model="gpt-4o", temperature=0)


def prepare_model_inputs(state: dict) -> list[dict]:
    # Retrieve user memories and add them to the system message
    # This function is called **every time** the model is prompted.
    # It converts the state to a prompt
    human_message = state["messages"][-1].content
    relevant_context = search_storage.invoke({"query": human_message})
    system_msg = f"[RAG Context]\n{relevant_context}\n[End of RAG Context]"
    return [{"role": "system", "content": system_msg}] + state["messages"]


@tool
def scrape_website(url: str) -> str:
    """Scrape a website and return the content"""
    loader = WebBaseLoader(url)
    doc = loader.load()[0]
    return f"{json.dumps(doc.metadata, indent=2)}\n{doc.page_content}"


graph = create_react_agent(
    llm,
    tools=[scrape_website, add_to_storage, search_storage],
    prompt=prepare_model_inputs,
)

if __name__ == "__main__":

    def print_stream(graph, message):  # noqa: ANN001, ANN201
        inputs = {"messages": [message]}
        for s in graph.stream(inputs, stream_mode="values"):
            # TODO: print the system message too
            message = s["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()

    print_stream(graph, "Store website https://www.example.com/")
    print_stream(graph, "Do I need permission to use that domain?")
