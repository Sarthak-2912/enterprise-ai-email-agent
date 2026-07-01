import json
import os
from urllib import response

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class IntentExtractor:

    def extract(self, prompt):

        system_prompt = """
You are an enterprise email assistant.

Extract:

1. department
2. instruction

Return ONLY valid JSON.

Example:

{
    "department":"Marketing",
    "instruction":"Tomorrow is Work From Home."
}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_prompt}\n\nUser: {prompt}"
        )

        cleaned = response.text.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned.replace("```json", "", 1)

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        return json.loads(cleaned)