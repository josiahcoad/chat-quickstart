setup-env:
	uv venv
	uv pip install -e ".[dev]"

demo:
	python agents/helloworld/helloworld_agent.py

dev:
	langgraph dev

precommit:
	pre-commit run --all-files

test:
	python clients/client.py
