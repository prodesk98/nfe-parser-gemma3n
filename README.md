# NF-e Parser using Gemma3n

A FastAPI application for parsing Brazilian electronic invoices (NF-e - Nota Fiscal Eletrônica) from images using the Gemma3n language model.

## Description

This project provides an API that extracts structured data from NF-e document images. It uses the Ollama API with the Gemma3n model to perform optical character recognition (OCR) and structured data extraction, converting the visual information from NF-e documents into a well-defined JSON format.

## Features

- Extract comprehensive NF-e data from images
- Structured output with detailed invoice information
- REST API with FastAPI
- Docker containerization for easy deployment
- GPU acceleration support

## Requirements

- Python 3.12 or higher
- Docker and Docker Compose (for containerized deployment)
- NVIDIA GPU (optional, for improved performance)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nfe-parser-gemma3n.git
   cd nfe-parser-gemma3n
   ```

2. Create a `.env` file from the template:
   ```bash
   cp template.env .env
   ```

3. Edit the `.env` file with your configuration:
   ```
   OLLAMA_API_URL=http://ollama:11434
   OLLAMA_API_KEY=your-ollama-api-key (if required)
   OLLAMA_MODEL=gemma3n:e4b
   ```

4. Start the application with Docker Compose:
   ```bash
   docker-compose up -d
   ```

### Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nfe-parser-gemma3n.git
   cd nfe-parser-gemma3n
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # OR
   source .venv/bin/activate  # On Unix/macOS
   
   pip install uv
   uv pip install -e .
   ```

3. Create a `.env` file from the template:
   ```bash
   cp template.env .env
   ```

4. Edit the `.env` file with your configuration:
   ```
   OLLAMA_API_URL=http://localhost:11434
   OLLAMA_API_KEY=your-ollama-api-key (if required)
   OLLAMA_MODEL=gemma3n:e4b
   ```

5. Start the application:
   ```bash
   fastapi dev main.py
   ```

## Usage

### API Endpoint

The API provides a single endpoint for parsing NF-e images:

- **POST /parse**
  - Accepts a multipart/form-data request with an image file
  - Returns the structured NF-e data in JSON format

### Example Request

Using curl:

```bash
curl -X POST "http://localhost:8000/parse" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "image=@path/to/your/nfe-image.jpg"
```

Using Python requests:

```python
import requests

url = "http://localhost:8000/parse"
files = {"image": open("path/to/your/nfe-image.jpg", "rb")}

response = requests.post(url, files=files)
nfe_data = response.json()
print(nfe_data)
```

### Response Structure

The API returns a structured JSON object containing the parsed NF-e data, including:

- Invoice identification details
- Issuer information
- Recipient information
- Product details with tax information
- Invoice totals
- Transportation information
- Billing and payment details
- Additional information

## Configuration

The application can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| OLLAMA_API_URL | URL of the Ollama API | http://localhost:11434 |
| OLLAMA_API_KEY | API key for Ollama (if required) | None |
| OLLAMA_MODEL | Ollama model to use | gemma3n:e4b |

## Project Structure

- `main.py` - FastAPI application entry point
- `core.py` - Core functionality for parsing NF-e images
- `schemas.py` - Pydantic models defining the NF-e data structure
- `environment.py` - Environment configuration
- `Dockerfile` - Container definition
- `docker-compose.yaml` - Multi-container Docker configuration

## Dependencies

- FastAPI - Web framework for building APIs
- langchain-ollama - Interface to Ollama language models
- Pillow - Image processing library
- Pydantic - Data validation and settings management
- python-dotenv - Environment variable management

## License

[CC0-1.0 license](LICENSE)