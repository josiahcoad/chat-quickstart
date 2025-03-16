from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from practical_sequential_graph import create_text_analysis_graph

# Import LangGraph examples
from sequential_graph_example import (
    create_empty_sequence_graph,
    create_explicit_sequential_graph,
    create_sequence_shorthand_graph,
)

# Create FastAPI app
app = FastAPI(
    title="LangGraph Sequential API",
    description="API for interacting with LangGraph sequential graphs",
    version="0.1.0",
)


# Input model definitions
class BasicGraphInput(BaseModel):
    input: str


class TextAnalysisInput(BaseModel):
    text: str


# Response model definitions
class BasicGraphResponse(BaseModel):
    input: str
    step1_result: str
    step2_result: str
    step3_result: str


class TextAnalysisResponse(BaseModel):
    text: str
    preprocessed_text: str
    analyzed_sentiments: List[Dict[str, str]]
    summarized_text: str
    final_report: str


# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "LangGraph Sequential API",
        "endpoints": [
            "/docs",
            "/basic/explicit",
            "/basic/shorthand",
            "/basic/empty",
            "/practical/text-analysis",
        ],
    }


# Basic graph endpoints
@app.post("/basic/explicit", response_model=BasicGraphResponse)
def run_explicit_graph(data: BasicGraphInput):
    """
    Run the explicit sequential graph with the provided input.

    This graph demonstrates creating a sequential pipeline by explicitly defining nodes and edges.
    """
    try:
        app = create_explicit_sequential_graph()
        result = app.invoke({"input": data.input})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph execution failed: {str(e)}")


@app.post("/basic/shorthand", response_model=BasicGraphResponse)
def run_shorthand_graph(data: BasicGraphInput):
    """
    Run the shorthand sequential graph with the provided input.

    This graph demonstrates creating a sequential pipeline using the add_sequence shorthand.
    """
    try:
        app = create_sequence_shorthand_graph()
        result = app.invoke({"input": data.input})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph execution failed: {str(e)}")


@app.post("/basic/empty", response_model=BasicGraphResponse)
def run_empty_graph(data: BasicGraphInput):
    """
    Run the empty sequence graph with the provided input.

    This graph demonstrates creating a sequential pipeline starting with an empty graph.
    """
    try:
        app = create_empty_sequence_graph()
        result = app.invoke({"input": data.input})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph execution failed: {str(e)}")


# Practical example endpoint
@app.post("/practical/text-analysis", response_model=TextAnalysisResponse)
def run_text_analysis(data: TextAnalysisInput):
    """
    Run the text analysis pipeline with the provided text.

    This graph demonstrates a more practical example with text preprocessing,
    sentiment analysis, summarization, and report generation.
    """
    try:
        app = create_text_analysis_graph()
        result = app.invoke({"text": data.text})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph execution failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
