# LangGraph Sequential Graphs

This repository demonstrates how to create sequential graphs (pipelines) using LangGraph. A sequential graph represents a linear flow of operations where each node processes data and passes it to the next node in sequence.

## Requirements

- Python 3.13 or later
- UV package manager
- Make
- Docker and Docker Compose (for containerized deployment)

## Installation and Setup

```bash
# Install uv if you don't already have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Quick setup with make
make setup
```

The `make setup` command will:
- Install uv if not already installed
- Initialize the project
- Install project dependencies
- Install development dependencies
- Set up pre-commit hooks

## Docker Deployment

This project includes Docker support for containerized deployment, which simplifies dependency management and ensures consistent execution across different environments.

### Building and Running with Docker

```bash
# Build the Docker image using default Dockerfile
make docker-build

# OR build using the alternative Dockerfile with UV directly
make docker-build-alt

# Start the container
make docker-up

# View logs
make docker-logs

# Stop the container
make docker-down
```

The dockerized API server will be available at: http://localhost:8000

### Docker Configurations

The project provides two Dockerfile options:

1. **Default (Dockerfile)**: Uses pipx to install UV inside the container
2. **Alternative (Dockerfile.alt)**: Installs UV directly using curl and cargo

You can choose either option based on your preference. Both Dockerfiles:
- Use Python 3.13 slim as the base image
- Install project dependencies using UV package manager
- Mount your local directory to allow for live code changes
- Expose port 8000 for the API server

### Manual Docker Commands

If you prefer to use Docker commands directly:

```bash
# Build with default Dockerfile
docker-compose build

# Build with alternative Dockerfile
docker-compose -f docker-compose.yml -f docker-compose.alt.yml build

# Start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

### Docker Configuration

The project includes the following Docker configuration files:

- `Dockerfile`: Defines the container image
- `docker-compose.yml`: Configures the services
- `.dockerignore`: Excludes unnecessary files from the build context

The Docker setup uses Python 3.13 and installs all required dependencies automatically, making it easy to run the application without worrying about local Python versions or package conflicts.

## FastAPI Integration

This project includes a FastAPI application that exposes the LangGraph sequential graphs as REST API endpoints.

### Running the API Server

```bash
# Run the FastAPI server
make serve

# Or run in development mode with auto-reload
make serve-dev
```

The server will be available at: http://localhost:8000

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/docs` | GET | Interactive API documentation |
| `/basic/explicit` | POST | Run the basic sequential graph (explicit definition) |
| `/basic/shorthand` | POST | Run the basic sequential graph (shorthand definition) |
| `/basic/empty` | POST | Run the basic sequential graph (empty graph definition) |
| `/practical/text-analysis` | POST | Run the text analysis pipeline |

### Example API Usage

#### Basic Sequential Graph API

```bash
curl -X POST "http://localhost:8000/basic/explicit" \
     -H "Content-Type: application/json" \
     -d '{"input": "Hello LangGraph API!"}'
```

Response:
```json
{
  "input": "Hello LangGraph API!",
  "step1_result": "Processed input: Hello LangGraph API!",
  "step2_result": "Further processed: Processed input: Hello LangGraph API!",
  "step3_result": "Final processing: Further processed: Processed input: Hello LangGraph API!"
}
```

#### Text Analysis API

```bash
curl -X POST "http://localhost:8000/practical/text-analysis" \
     -H "Content-Type: application/json" \
     -d '{"text": "I really love this API. It works great!"}'
```

### Python Client Example

The project includes a sample Python client that demonstrates how to interact with the API:

```bash
# Run the client example (requires the API server to be running)
make client
```

This will:
1. Connect to the API server
2. Send requests to all the available endpoints
3. Display the formatted responses

You can also examine the `client_example.py` file to see how to make API calls from Python code.

## Development Workflow

All development tasks are available through Make commands. The most common are:

```bash
# Install dependencies
make install        # Install project dependencies
make install-dev    # Install development dependencies

# Code quality
make lint           # Run ruff check with auto-fix
make format         # Run ruff format
make type           # Run mypy type checking
make pylint         # Run pylint
make check          # Run all checks
make pre-commit     # Run all pre-commit hooks

# Examples
make run-examples   # Run all example scripts

# API server
make serve          # Run the FastAPI server
make serve-dev      # Run the server in development mode

# Maintenance
make clean          # Clean cache files
```

## Available Make Commands

For a complete list of commands, run:

```bash
make help
```

This will display:

```
Available commands:
  make setup         - Install uv and set up the development environment
  make install       - Install project dependencies
  make install-dev   - Install development dependencies
  make lint          - Run linting (ruff check)
  make format        - Run code formatting (ruff format)
  make type          - Run type checking (mypy)
  make pylint        - Run pylint
  make check         - Run all checks (lint, format, type, pylint)
  make pre-commit    - Run pre-commit on all files
  make run-examples  - Run the example scripts
  make clean         - Clean up temporary files and caches
  make serve         - Run the FastAPI server
  make serve-dev     - Run the server in development mode
```

## Tool Configuration

All tools are configured in pyproject.toml for centralized management:

- **Ruff**: Linting and formatting ([tool.ruff])
- **mypy**: Type checking ([tool.mypy])
- **pylint**: Additional linting ([tool.pylint])

## Basic Sequential Graph

The file `sequential_graph_example.py` demonstrates three different methods for creating a simple sequential graph:

1. **Explicit Node and Edge Definition**:
   ```python
   graph = StateGraph(State)

   # Add nodes
   graph.add_node("step1", step1)
   graph.add_node("step2", step2)
   graph.add_node("step3", step3)

   # Connect the nodes in sequence
   graph.add_edge("step1", "step2")
   graph.add_edge("step2", "step3")
   graph.add_edge("step3", END)

   # Set the entry point
   graph.set_entry_point("step1")
   ```

2. **Using add_sequence Shorthand**:
   ```python
   graph = StateGraph(State)

   # Add a sequence of nodes
   graph.add_sequence("step1", [step1, step2, step3])
   ```

3. **Starting with an Empty Graph**:
   ```python
   graph = StateGraph(State)

   # Define the sequence of nodes
   nodes = [
       ("step1", step1),
       ("step2", step2),
       ("step3", step3)
   ]

   # Add the sequence
   graph.add_sequence("step1", [node[1] for node in nodes])
   ```

## Practical Example: Text Analysis Pipeline

The file `practical_sequential_graph.py` demonstrates a more practical example of a text analysis pipeline with the following steps:

1. **Text Preprocessing**: Clean and normalize text
2. **Sentiment Analysis**: Identify positive and negative words
3. **Text Summarization**: Generate a summary of the text
4. **Report Generation**: Create a final report

This example shows how to:
- Define a complex state with multiple fields
- Create node functions that process specific parts of the state
- Chain these functions together in a sequential graph
- Run the graph and inspect results

## Running Individual Examples

While you can use `make run-examples` to run all examples, you can also run them individually:

```bash
# Run with uv
uv run --python 3.13 sequential_graph_example.py
uv run --python 3.13 practical_sequential_graph.py

# Run with explicit dependency installation
uv run --python 3.13 --with langgraph sequential_graph_example.py
```

## Advanced UV Commands

For advanced users, here are some useful UV commands:

```bash
# Initialize a new project
uv init

# Add specific packages
uv add langgraph
uv add numpy pandas matplotlib  # Add multiple packages at once

# Install from requirements.txt
uv pip install -r requirements.txt

# Create a lockfile
uv lock

# Run a command in the virtual environment
uv run pytest
```

## Key Concepts

- **StateGraph**: The main class for creating a graph in LangGraph
- **State**: A TypedDict that defines the structure of the data flowing through the graph
- **Node Functions**: Functions that process the state and return updates
- **END**: A special constant that indicates the end of the graph
- **add_sequence**: A convenient method for creating a linear sequence of nodes

## Tips for Creating Sequential Graphs

1. Define your state clearly with all necessary fields
2. Make each node function focus on a specific task
3. Ensure each function returns only the fields it updates
4. For simple sequences, use `add_sequence` for cleaner code
5. For more complex graphs, explicitly define nodes and edges
