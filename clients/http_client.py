import os
import requests


def call_assistant_api(
    assistant_id: str,
    input_data: dict,
    metadata: dict | None = None,
    config: dict | None = None,
) -> dict:
    headers = {"X-Api-Key": os.environ["LANGSMITH_API_KEY"]}
    payload = {
        "thread_id": None,
        "assistant_id": assistant_id,
        "input": input_data,
    }
    if metadata:
        payload["metadata"] = metadata
    if config:
        payload["config"] = {"configurable": config}

    response = requests.post(
        f"http://localhost:2024/runs/wait",
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    return response.json()


result = call_assistant_api(
    assistant_id="agent",
    input_data={"messages": [("user", "What's 2 + 2?")]},
)
print(result["messages"][-1]["content"])  # type: ignore[index]
