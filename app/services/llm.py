from google import genai
from app.config import GEMINI_API_KEY, MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_llm(message: str):

    response = client.models.generate_content(model=MODEL, contents=message)

    return response.text
