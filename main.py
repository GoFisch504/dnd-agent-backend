from fastapi import FastAPI
from routes import characters, sessions

app = FastAPI()

app.include_router(characters.router)
app.include_router(sessions.router)
