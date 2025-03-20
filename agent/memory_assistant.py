from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.runnables.config import RunnableConfig
from langgraph.prebuilt import InjectedStore, create_react_agent
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore

load_dotenv()


def save_memory(
    memory: str,
    *,
    config: RunnableConfig,
    store: Annotated[BaseStore, InjectedStore()],
) -> str:
    """Save the given memory for the current user."""
    # This is a **tool** the model can use to save memories to storage
    user_id = config.get("configurable", {}).get("user_id") or "user1"
    namespace = ("memories", user_id)
    store.put(namespace, f"memory_{len(store.search(namespace))}", {"data": memory})
    return f"Saved memory: {memory}"


async def prepare_model_inputs(
    state: dict,
    config: RunnableConfig,
    store: BaseStore,
) -> list[dict]:
    # Retrieve user memories and add them to the system message
    # This function is called **every time** the model is prompted.
    # It converts the state to a prompt
    user_id = config.get("configurable", {}).get("user_id") or "user1"
    namespace = ("memories", user_id)
    memories = [m.value["data"] for m in await store.asearch(namespace)]
    system_msg = f"User memories: {', '.join(memories)}"
    return [{"role": "system", "content": system_msg}] + state["messages"]


model = init_chat_model(model="gpt-4o", temperature=0)
store = InMemoryStore()

graph = create_react_agent(
    model,
    [save_memory],
    prompt=prepare_model_inputs,
    store=store,
)


if __name__ == "__main__":

    def print_stream(graph, message, config):  # noqa: ANN001, ANN201
        inputs = {"messages": [message]}
        for s in graph.stream(inputs, config, stream_mode="values"):
            message = s["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()

    config = {"configurable": {"thread_id": "thread-1", "user_id": "1"}}
    print_stream(graph, "Remember that my name is John Doe", config)
    print_stream(graph, "What do you remmeber about me?", config)
