setup-env:
	uv venv
	uv pip install -e ".[dev]"

demo:
	python agents/1_basic/assistant.py

dev:
	langgraph dev


precommit:
	pre-commit run --all-files

test:
	python -m pytest tests/unit/
