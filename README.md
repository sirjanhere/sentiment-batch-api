# Sentiment Batch API

A FastAPI project for batch sentiment analysis. Accepts multiple sentences and returns their sentiment as `happy`, `sad`, or `neutral`.

## Features

- Batch sentiment analysis endpoint
- Simple rule-based sentiment model
- FastAPI backend
- CORS enabled
- Works with localhost for testing
- Compatible with automated evaluation systems

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

If you don’t have a virtual environment yet:

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

## Run the API

Start the server using:

```bash
uvicorn main:app --reload
```

Server will start at:

http://localhost:8000

API docs (Swagger UI) available at:

http://localhost:8000/docs

## API Endpoints

1. Health Check  
   GET /

   Response:

   ```json
   {
     "message": "Send POST request to /sentiment with {'sentences': [...]}"
   }
   ```

2. Sentiment Analysis (Main Endpoint)  
   POST /sentiment

   Request Body (JSON):

   ```json
   {
     "sentences": [
       "I love programming!",
       "This is frustrating.",
       "I'm fine today."
     ]
   }
   ```

   Response:

   ```json
   {
     "results": [
       { "sentence": "I love programming!", "sentiment": "happy" },
       { "sentence": "This is frustrating.", "sentiment": "sad" },
       { "sentence": "I'm fine today.", "sentiment": "neutral" }
     ]
   }
   ```

## Test with Postman

Open Postman and:

- Choose POST
- URL: http://localhost:8000/sentiment
- Go to Body → raw → JSON
- Enter:

```json
{
  "sentences": [
    "I enjoy learning new things.",
    "This is the worst day.",
    "What time is the meeting?"
  ]
}
```

## Test with cURL (optional)

```bash
curl -X POST "http://localhost:8000/sentiment" \
  -H "Content-Type: application/json" \
  -d "{\"sentences\": [\"I love this\", \"This is bad\"]}"
```

## Folder Structure

sentiment-batch-api/
├── main.py
├── requirements.txt
├── README.md

## Notes

- This API allows CORS from all origins for testing flexibility.
- Supports fallback POST to `/` for compatibility with some evaluation portals.
- No external ML model required — the API uses a simple rule-based sentiment fallback suitable for small-scale/baseline evaluation.
