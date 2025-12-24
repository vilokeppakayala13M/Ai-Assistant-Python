import os
from pathlib import Path
from dotenv import load_dotenv

# Robustly find .env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# AI Configuration
# Supported types: 'gemini', 'openai'
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Voice Configuration
VOICE_ID = 0  # Index of the voice to use (0 is usually default)
SPEAK_RATE = 175  # Words per minute
WAKE_WORD = "batman"
