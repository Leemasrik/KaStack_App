from fastapi import FastAPI

from models import ChatRequest
from response_generator import generate_response

app = FastAPI()


@app.post("/chat")
def chat(request: ChatRequest):

    return generate_response(request)