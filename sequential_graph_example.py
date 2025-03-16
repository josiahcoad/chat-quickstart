from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END


# Define our state
class State(TypedDict):
    input: str
    step1_result: str
    step2_result: str
    step3_result: str


# Define our node functions
def step1(state: State) -> Dict:
    """First step in our sequence."""
    return {"step1_result": f"Processed input: {state['input']}"}


def step2(state: State) -> Dict:
    """Second step in our sequence."""
    return {"step2_result": f"Further processed: {state['step1_result']}"}


def step3(state: State) -> Dict:
    """Third step in our sequence."""
    return {"step3_result": f"Final processing: {state['step2_result']}"}


# METHOD 1: Building a sequential graph explicitly
def create_explicit_sequential_graph():
    """Create a sequential graph by explicitly defining nodes and edges."""
    # Initialize the graph
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

    # Compile the graph
    app = graph.compile()

    return app


# METHOD 2: Using the convenient add_sequence method
def create_sequence_shorthand_graph():
    """Create a sequential graph using the add_sequence shorthand."""
    # Initialize the graph
    graph = StateGraph(State)

    # Add a sequence of nodes
    nodes = [step1, step2, step3]
    graph.add_sequence(nodes)

    # Compile the graph
    app = graph.compile()

    return app


# METHOD 3: Start with an empty graph and add sequence with nodes
def create_empty_sequence_graph():
    """Create a sequential graph starting with an empty graph."""
    # Initialize the graph
    graph = StateGraph(State)

    # Define the sequence of nodes
    nodes = [
        step1,
        step2,
        step3,
    ]

    # Add the sequence
    graph.add_sequence(nodes)

    # Compile the graph
    app = graph.compile()

    return app


# Example usage
if __name__ == "__main__":
    # Create the graph using any of the methods
    app = create_explicit_sequential_graph()
    # app = create_sequence_shorthand_graph()
    # app = create_empty_sequence_graph()

    # Run the graph with initial input
    result = app.invoke({"input": "Hello LangGraph!"})
    print(result)
