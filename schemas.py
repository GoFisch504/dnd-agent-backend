from pydantic import BaseModel
from typing import List, Dict

class CharacterSchema(BaseModel):
    name: str
    class_: str
    level: int
    stats: Dict[str, int]
    inventory: List[str]

class SessionNoteSchema(BaseModel):
    date: str
    notes: str
