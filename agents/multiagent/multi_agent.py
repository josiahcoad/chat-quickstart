from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm

model = init_chat_model(model="gpt-4o")


def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
    ----
        a: The first number.
        b: The second number.

    Returns:
    -------
        The sum of the two numbers.

    """
    return a + b


alice = create_react_agent(
    model,
    [add, create_handoff_tool(agent_name="Bob")],
    prompt="You are Alice, an addition expert.",
    name="Alice",
)

bob = create_react_agent(
    model,
    [
        create_handoff_tool(
            agent_name="Alice",
            description="Transfer to Alice, she can help with math",
        ),
    ],
    prompt="You are Bob, you speak like a pirate.",
    name="Bob",
)

checkpointer = InMemorySaver()
workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice",
)
graph = workflow.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    config = RunnableConfig({"configurable": {"thread_id": "1"}})
    turn_1 = graph.invoke(
        {"messages": [{"role": "user", "content": "i'd like to speak to Bob"}]},
        config,
    )
    print(turn_1)

    turn_2 = graph.invoke(
        {"messages": [{"role": "user", "content": "what's 5 + 7?"}]},
        config,
    )
    print(turn_2)
