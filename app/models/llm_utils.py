import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_ENDPOINT = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")  # replace with your-together-api-key


def generate_speaking_response(caption: str, band: str, api_key=None) -> str:
    prompt = f"""
    You are a CELPIP or PTE English Speaking Test Coach.

    The following image has been described as:
    "{caption}"

    Your task is to generate a test-style speaking response at Band {band} level.

    Do NOT include any introductory or conversational phrases like: “Sure, let's describe it.”

    Just provide the actual fluent and natural spoken response — nothing else.

    Keep it clear, concise, and appropriate for Band {band} level.
    """

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(TOGETHER_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError:
        if response.status_code == 401 or response.status_code == 403:
            return "❌ Invalid or missing Together.AI API key."
        else:
            return f"❌ HTTP Error"
    except Exception:
        return f"❌ Unexpected error"
