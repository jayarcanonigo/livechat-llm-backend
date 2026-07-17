import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-3.5-flash",
]


def ask_gemini(message: str):
    last_error = None

    for model in MODELS:
        try:
            print(f"Trying model: {model}")

            response = client.models.generate_content(
                model=model,
                contents=message,
            )

            return response.text

        except (errors.ServerError, errors.ClientError) as e:
            print(f"{model} failed: {e}")
            last_error = e

    return f"All Gemini models failed: {last_error}"
