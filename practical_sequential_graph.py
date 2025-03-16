from typing import Dict, List, TypedDict
from langgraph.graph import StateGraph, END


# Define our state
class State(TypedDict):
    text: str
    preprocessed_text: str
    analyzed_sentiments: List[Dict]
    summarized_text: str
    final_report: str


# Define node functions
def preprocess_text(state: State) -> Dict:
    """Preprocess the text by removing extra spaces and converting to lowercase."""
    text = state["text"]
    preprocessed = text.strip().lower()

    # In a real application, you would do more sophisticated preprocessing
    # such as removing stopwords, stemming, etc.

    return {"preprocessed_text": preprocessed}


def analyze_sentiment(state: State) -> Dict:
    """Analyze sentiment of the preprocessed text."""
    text = state["preprocessed_text"]

    # This is a simple mock implementation
    # In a real app, you would use a proper NLP model
    positive_words = ["good", "great", "excellent", "happy", "like", "love"]
    negative_words = ["bad", "terrible", "awful", "sad", "dislike", "hate"]

    words = text.split()
    sentiments = []

    for word in words:
        if word in positive_words:
            sentiments.append({"word": word, "sentiment": "positive"})
        elif word in negative_words:
            sentiments.append({"word": word, "sentiment": "negative"})

    return {"analyzed_sentiments": sentiments}


def summarize_text(state: State) -> Dict:
    """Generate a summary based on the preprocessed text."""
    text = state["preprocessed_text"]

    # This is a simple mock implementation
    # In a real app, you would use a proper summarization model
    if len(text) > 100:
        summary = text[:100] + "..."
    else:
        summary = text

    return {"summarized_text": summary}


def generate_report(state: State) -> Dict:
    """Generate a final report combining sentiments and summary."""
    sentiments = state["analyzed_sentiments"]
    summary = state["summarized_text"]

    # Count sentiments
    positive_count = sum(1 for s in sentiments if s["sentiment"] == "positive")
    negative_count = sum(1 for s in sentiments if s["sentiment"] == "negative")

    # Generate report
    report = f"SUMMARY: {summary}\n\n"
    report += f"SENTIMENT ANALYSIS:\n"
    report += f"- Positive words: {positive_count}\n"
    report += f"- Negative words: {negative_count}\n"

    if positive_count > negative_count:
        report += f"Overall sentiment: Positive"
    elif negative_count > positive_count:
        report += f"Overall sentiment: Negative"
    else:
        report += f"Overall sentiment: Neutral"

    return {"final_report": report}


# Create the sequential graph
def create_text_analysis_graph():
    """Create a text analysis pipeline as a sequential graph."""
    # Initialize the graph
    graph = StateGraph(State)

    # Method 1: Add nodes and edges explicitly
    graph.add_node("preprocess", preprocess_text)
    graph.add_node("analyze_sentiment", analyze_sentiment)
    graph.add_node("summarize", summarize_text)
    graph.add_node("generate_report", generate_report)

    # Connect nodes in sequence
    graph.add_edge("preprocess", "analyze_sentiment")
    graph.add_edge("analyze_sentiment", "summarize")
    graph.add_edge("summarize", "generate_report")
    graph.add_edge("generate_report", END)

    # Set entry point
    graph.set_entry_point("preprocess")

    # Compile the graph
    app = graph.compile()

    return app


# Example usage
if __name__ == "__main__":
    # Create the graph
    app = create_text_analysis_graph()

    # Alternative way to create the graph using add_sequence:
    # graph = StateGraph(State)
    # graph.add_sequence(
    #     "preprocess",
    #     [preprocess_text, analyze_sentiment, summarize_text, generate_report]
    # )
    # app = graph.compile()

    # Sample text
    sample_text = "I really love this product. It's great and works well. However, the delivery was terrible and I hate the packaging."

    # Run the graph
    result = app.invoke({"text": sample_text})

    # Print final report
    print("\n" + "=" * 50)
    print("TEXT ANALYSIS RESULT")
    print("=" * 50)
    print(result["final_report"])
    print("=" * 50)

    # You can also see the complete state for debugging
    print("\nComplete state:")
    print(f"Original text: {result['text']}")
    print(f"Preprocessed text: {result['preprocessed_text']}")
    print(f"Analyzed sentiments: {result['analyzed_sentiments']}")
    print(f"Summarized text: {result['summarized_text']}")
