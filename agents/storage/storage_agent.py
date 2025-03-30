import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState

from agents.storage.tools import add_to_storage, get_from_storage, get_storage_index

load_dotenv()

llm = init_chat_model(model="gpt-4o", temperature=0)


async def prepare_model_inputs(state: AgentState) -> list[dict[str, str] | BaseMessage]:
    kb_index = get_storage_index()
    system_msg = f"[Knowledge Base]\n{kb_index}"
    past_messages: Sequence[BaseMessage] = state["messages"]
    return [{"role": "system", "content": system_msg}, *past_messages]


@tool
def scrape_website(url: str) -> str:
    """Scrape a website and return the content.

    Args:
    ----
        url: The URL of the website to scrape.

    """
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

    async def demo() -> None:
        response = await graph.ainvoke(
            {"messages": [("user", "Store website https://www.example.com/")]},
        )
        print(response["messages"][-1].content, "\n", "-" * 100)

        response = await graph.ainvoke(
            {"messages": [("user", "What is stored in my knowledge base?")]},
        )
        print(response["messages"][-1].content)

    asyncio.run(demo())
