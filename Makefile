setup-env:
	uv venv
	uv pip install ".[dev]"

test:
	python agent/assistant.py

dev:
	langgraph dev

