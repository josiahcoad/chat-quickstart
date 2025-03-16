#!/usr/bin/env python3
"""
Example Python client for the LangGraph Sequential API.

This script demonstrates how to interact with the API endpoints
using the requests library.
"""

import json
import sys

import requests

API_BASE_URL = "http://localhost:8000"


def print_response(response):
    """Print the response in a formatted way."""
    print("\nStatus code:", response.status_code)
    print("Response:")
    try:
        formatted_json = json.dumps(response.json(), indent=2)
        print(formatted_json)
    except json.JSONDecodeError:
        print(response.text)


def run_basic_graph():
    """Demonstrate basic sequential graph API endpoints."""
    print("\n=== Running Basic Sequential Graph Examples ===")

    input_data = {"input": "Hello from the Python client!"}

    # Test each graph variant
    endpoints = ["/basic/explicit", "/basic/shorthand", "/basic/empty"]

    for endpoint in endpoints:
        print(f"\nCalling {endpoint}...")
        response = requests.post(
            f"{API_BASE_URL}{endpoint}", json=input_data, timeout=10
        )
        print_response(response)


def run_text_analysis():
    """Demonstrate text analysis API endpoint."""
    print("\n=== Running Text Analysis Pipeline Example ===")

    text = (
        "I really love this API client. It's amazing and works well. "
        "However, I do have some concerns about performance."
    )

    input_data = {"text": text}

    print("\nCalling /practical/text-analysis...")
    response = requests.post(
        f"{API_BASE_URL}/practical/text-analysis", json=input_data, timeout=10
    )
    print_response(response)


def main():
    """Main function to demonstrate API usage."""
    print("LangGraph Sequential API Client Example")
    print("--------------------------------------")
    print(f"Using API at: {API_BASE_URL}")

    try:
        # Check if API is running
        health_check = requests.get(API_BASE_URL, timeout=5)
        if health_check.status_code == 200:
            print("API server is running!")

            # Run the examples
            run_basic_graph()
            run_text_analysis()
        else:
            print(
                f"\nERROR: API server returned status code {health_check.status_code}"
            )
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("\nERROR: Cannot connect to the API server.")
        print("Make sure the server is running with: make serve")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("\nERROR: Connection to the API server timed out.")
        print("Make sure the server is running and responsive.")
        sys.exit(1)


if __name__ == "__main__":
    main()
