import json

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from agent.tools.storage import add_to_storage, get_from_storage, get_storage_index

load_dotenv()

llm = init_chat_model(model="gpt-4o", temperature=0)


async def prepare_model_inputs(state: dict) -> list[dict]:
    kb_index = get_storage_index()
    system_msg = f"[Knowledge Base]\n{kb_index}"
    return [{"role": "system", "content": system_msg}] + state["messages"]


@tool
def scrape_website(url: str) -> str:
    """Scrape a website and return the content"""
    loader = WebBaseLoader(url)
    doc = loader.load()[0]
    return f"{json.dumps(doc.metadata, indent=2)}\n{doc.page_content}"


graph = create_react_agent(
    llm,
    tools=[scrape_website, add_to_storage, get_from_storage],
    prompt=prepare_model_inputs,  # type: ignore[arg-type]
)


if __name__ == "__main__":
    import asyncio

    async def demo():  # noqa: ANN201
        response = await graph.ainvoke(
            {"messages": [("user", "Store website https://www.example.com/")]},
        )
        print(response["messages"][-1].content, "\n", "-" * 100)

        response = await graph.ainvoke(
            {"messages": [("user", "What is stored in my knowledge base?")]},
        )
        print(response["messages"][-1].content)

    asyncio.run(demo())
