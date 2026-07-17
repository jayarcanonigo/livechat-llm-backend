from pathlib import Path
from dotenv import load_dotenv
from google import genai
import os

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Models supporting generateContent:\n")

for m in client.models.list():
    methods = getattr(m, "supported_actions", None) or getattr(
        m, "supported_generation_methods", []
    )
    if "generateContent" in methods:
        print(m.name)
