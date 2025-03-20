from langchain_core.tools import tool


@tool
def add(x: float, y: float) -> float:
    """Add two numbers together

    Args:
        x: The first number
        y: The second number

    Returns:
        The sum of the two numbers
    """
    return x + y


@tool
def subtract(x: float, y: float) -> float:
    """Subtract two numbers

    Args:
        x: The first number
        y: The second number

    Returns:
        The difference of the two numbers
    """
    return x - y
