# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Accept either direct Gemini or OpenRouter fallback
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
APIFY_TOKEN = os.getenv("APIFY_TOKEN")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise ValueError("CRITICAL SETUP FAILURE: Either GEMINI_API_KEY or OPENROUTER_API_KEY must be defined.")
    
if not APIFY_TOKEN:
    raise ValueError("CRITICAL SETUP FAILURE: APIFY_TOKEN must be defined inside your .env file.")