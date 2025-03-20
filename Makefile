setup:
	uv venv
	uv pip install -e .
	uv pip install -e ".[dev]"

test:
	python agent/assistant.py

dev:
	langgraph dev

