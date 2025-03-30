"""This client uses the LangGraph SDK to interact with the LangGraph server."""

from langgraph_sdk import get_sync_client

# make sure to run `langgraph dev` before running this script
langgraph_client = get_sync_client(url="http://localhost:2024")

run = langgraph_client.runs.wait(
    thread_id=None,
    assistant_id="agent",
    input={
        "messages": [("user", "What's 2 + 2?")],
    },
)

print(run["messages"][-1]["content"])  # type: ignore[call-overload]
