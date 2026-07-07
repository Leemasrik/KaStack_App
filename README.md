# Mock AI Backend - Phase 1

## Overview

This project is a Phase 1 mock backend for the AI Chat Application.

Instead of calling Gemini, the backend returns predefined (hardcoded) responses. This allows the Android application to integrate and test the complete request-response flow before actual AI integration.

## Features

- FastAPI backend
- POST `/chat` endpoint
- Accepts user message and local memory
- Returns hardcoded AI response
- Returns `memory_update` structure for future phases

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Project Structure

```
.
├── app.py
├── response_generator.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST `/chat`

### Sample Request

```json
{
  "message": "Tomorrow I have OOPS exam",
  "personality": [],
  "events": [],
  "hobbies": []
}
```

### Sample Response

```json
{
  "reply": "You have an OOPS exam tomorrow. Revise OOP concepts for 2 hours today.",
  "memory_update": {
    "personality": [],
    "events": [],
    "hobbies": []
  }
}
```

## Current Phase

✅ Phase 1

- Mock AI responses
- No Gemini integration
- No database logging
- API contract finalized

## Upcoming Phases

### Phase 2
- Integrate Gemini API
- Generate dynamic responses

### Phase 3
- Memory extraction
- SQLite updates
- Supabase logging
- Production-ready workflow