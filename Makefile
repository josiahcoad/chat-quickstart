.PHONY: setup install install-dev lint format type check run-examples clean help serve serve-dev client docker-build docker-build-alt docker-up docker-down docker-logs

PYTHON = python3.13
UV = uv
RUFF = ruff
MYPY = mypy
PYLINT = pylint
PRE_COMMIT = pre-commit
PORT = 8000
HOST = 0.0.0.0

help:
	@echo "LangGraph Sequential Graphs - Development Commands"
	@echo ""
	@echo "Setup and Installation:"
	@echo "  make setup         - Install uv and set up the development environment"
	@echo "  make install       - Install project dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint          - Run linting (ruff check)"
	@echo "  make format        - Run code formatting (ruff format)"
	@echo "  make type          - Run type checking (mypy)"
	@echo "  make pylint        - Run pylint"
	@echo "  make check         - Run all checks (lint, format, type, pylint)"
	@echo "  make pre-commit    - Run pre-commit on all files"
	@echo ""
	@echo "Examples:"
	@echo "  make run-examples  - Run the example scripts"
	@echo ""
	@echo "API Server:"
	@echo "  make serve         - Run the FastAPI server"
	@echo "  make serve-dev     - Run the FastAPI server in development mode (with reload)"
	@echo "  make client        - Run the API client example script"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build  - Build the Docker image using the default Dockerfile"
	@echo "  make docker-build-alt - Build the Docker image using the alternative Dockerfile with UV"
	@echo "  make docker-up     - Start the Docker container"
	@echo "  make docker-down   - Stop the Docker container"
	@echo "  make docker-logs   - View the Docker container logs"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean         - Clean up temporary files and caches"
	@echo ""
	@echo "Tool Configuration:"
	@echo "  All tools are configured in pyproject.toml:"
	@echo "  - Ruff: [tool.ruff] - Linting and formatting"
	@echo "  - MyPy: [tool.mypy] - Type checking"
	@echo "  - PyLint: [tool.pylint] - Additional linting"
	@echo ""
	@echo "For more detailed documentation, see README.md"

setup:
	@echo "Installing uv if needed..."
	@if ! command -v $(UV) &> /dev/null; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		export PATH="$$HOME/.cargo/bin:$$PATH"; \
	fi
	@echo "Installing dependencies..."
	@$(UV) init
	@$(UV) pip install -e .
	@$(UV) pip install -e ".[dev]"
	@$(PRE_COMMIT) install

install:
	@echo "Installing project dependencies..."
	@$(UV) pip install -e .

install-dev:
	@echo "Installing development dependencies..."
	@$(UV) pip install -e ".[dev]"

lint:
	@echo "Running ruff check..."
	@$(RUFF) check --fix .

format:
	@echo "Running ruff format..."
	@$(RUFF) format .

type:
	@echo "Running mypy type checking..."
	@$(MYPY) --python-version=3.13 .

pylint:
	@echo "Running pylint..."
	@$(PYLINT) --rcfile=pyproject.toml .

check: lint format type pylint
	@echo "All checks passed!"

pre-commit:
	@echo "Running pre-commit on all files..."
	@$(PRE_COMMIT) run --all-files

run-examples:
	@echo "Running examples..."
	@$(UV) run --python 3.13 sequential_graph_example.py
	@$(UV) run --python 3.13 practical_sequential_graph.py

serve:
	@echo "Starting FastAPI server on http://$(HOST):$(PORT)..."
	@$(UV) run --python 3.13 app.py

serve-dev:
	@echo "Starting FastAPI server in development mode on http://$(HOST):$(PORT)..."
	@$(UV) run --python 3.13 uvicorn app:app --host $(HOST) --port $(PORT) --reload

client:
	@echo "Running API client example..."
	@$(UV) run --python 3.13 client_example.py

docker-build:
	@echo "Building Docker image using default Dockerfile..."
	@docker-compose build

docker-build-alt:
	@echo "Building Docker image using alternative Dockerfile with UV..."
	@docker-compose -f docker-compose.yml -f docker-compose.alt.yml build

docker-up:
	@echo "Starting Docker container..."
	@docker-compose up -d
	@echo "API server running at http://localhost:$(PORT)"

docker-down:
	@echo "Stopping Docker container..."
	@docker-compose down

docker-logs:
	@echo "Viewing Docker container logs..."
	@docker-compose logs -f

clean:
	@echo "Cleaning up..."
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name .mypy_cache -exec rm -rf {} +
	@find . -type d -name .ruff_cache -exec rm -rf {} +
	@find . -type d -name .pytest_cache -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
