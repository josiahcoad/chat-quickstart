setup:
	uv venv
	uv pip install -e .
	uv pip install -e ".[dev]"
	source .venv/bin/activate

dev:
	langgraph dev

test:
	python agent/assistant.py
