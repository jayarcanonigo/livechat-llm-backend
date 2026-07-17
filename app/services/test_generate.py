from pathlib import Path
from dotenv import load_dotenv
from google import genai
import os

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

MODEL = os.getenv("MODEL")
API_KEY = os.getenv("GEMINI_API_KEY")

print("MODEL:", MODEL)

client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(model=MODEL, contents="Hello")

    print("SUCCESS")
    print(response.text)

except Exception as e:
    import traceback

    traceback.print_exc()
