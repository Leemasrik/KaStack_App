from pydantic import BaseModel
from typing import List, Dict, Any


class ChatRequest(BaseModel):
    message: str
    personality: List[Dict[str, Any]]
    events: List[Dict[str, Any]]
    hobbies: List[Dict[str, Any]]