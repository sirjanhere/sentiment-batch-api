from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import string

app = FastAPI()

# Allow all origins for testing portals
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class SentencesRequest(BaseModel):
    sentences: List[str]

# Response model
class SentimentResult(BaseModel):
    sentence: str
    sentiment: str

class SentimentResponse(BaseModel):
    results: List[SentimentResult]

# Improved sentiment analyzer
def analyze_sentiment(sentence: str) -> str:
    sentence_clean = sentence.lower()
    sentence_clean = sentence_clean.translate(str.maketrans("", "", string.punctuation))

    happy_words = [
        "love", "great", "amazing", "happy", "good", "excellent", "awesome",
        "like", "enjoy", "fantastic", "wonderful", "pleased", "nice", "cool",
        "best", "super", "positive", "fun"
    ]

    sad_words = [
        "sad", "bad", "terrible", "horrible", "worst", "upset", "angry",
        "hate", "disappointed", "awful", "poor", "negative", "sucks",
        "pain", "hurt", "cry", "depress"
    ]

    # Handle negations
    if "not good" in sentence_clean or "not happy" in sentence_clean:
        return "sad"
    if "not bad" in sentence_clean or "not sad" in sentence_clean:
        return "happy"

    # Strong negative words take priority
    if any(word in sentence_clean for word in sad_words):
        return "sad"

    # Positive words
    if any(word in sentence_clean for word in happy_words):
        return "happy"

    # Strong punctuation emotion
    if "!" in sentence:
        return "happy"

    return "neutral"

# Main endpoint
@app.post("/sentiment", response_model=SentimentResponse)
def sentiment_analysis(request: SentencesRequest):
    results = []
    for sentence in request.sentences:
        sentiment = analyze_sentiment(sentence)
        results.append(SentimentResult(sentence=sentence, sentiment=sentiment))
    return SentimentResponse(results=results)

# Support root fallback POST
@app.post("/", response_model=SentimentResponse)
def fallback_sentiment(request: SentencesRequest):
    results = []
    for sentence in request.sentences:
        sentiment = analyze_sentiment(sentence)
        results.append(SentimentResult(sentence=sentence, sentiment=sentiment))
    return SentimentResponse(results=results)

@app.get("/")
def root():
    return {"message": "Send POST request to /sentiment with {'sentences': [...]}"}
