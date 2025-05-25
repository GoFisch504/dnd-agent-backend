# D&D Agent Backend

This is a FastAPI-powered backend for a fully automated Dungeons & Dragons assistant. It supports:
- Character & session tracking
- Discord bot integration
- Audio recording/transcription (planned)
- Custom GPT integration with structured outputs

## 🚀 Getting Started

```bash
# Create and activate a virtual environment
python -m venv venv
.env\Scriptsctivate  # or source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
python -m uvicorn main:app --reload
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## 📁 Project Structure

- `main.py` - FastAPI entry point
- `routes/` - Character and session endpoints
- `models.py` - SQLAlchemy models
- `schemas.py` - Pydantic schemas
- `database.py` - DB connection config

## 🧙 Coming Soon

- Discord bot
- Session transcription with Whisper
- Web dashboard UI

