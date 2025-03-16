FROM python:3.13-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY pyproject.toml ./

# Install dependencies
RUN pip install --no-cache-dir pip --upgrade && \
    pip install --no-cache-dir hatchling && \
    pip install --no-cache-dir -e "." && \
    pip install --no-cache-dir -e ".[dev]"

# Copy application code
COPY . .

# Make the UV installation script executable
RUN chmod +x /app/install_uv.sh

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]

# Notes:
# - UV can be installed and used inside the container
# - To install UV inside the container, run:
#   docker-compose exec langgraph-api /app/install_uv.sh
