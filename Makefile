setup:
	uv venv
	uv pip install -e .
	uv pip install -e ".[dev]"
	source .venv/bin/activate

test:
	python agent/assistant.py

dev:
	langgraph dev

