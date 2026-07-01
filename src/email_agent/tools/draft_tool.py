import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class DraftTool:

    def draft(self, instruction):

        prompt = f"""
You are an enterprise email assistant.

Generate a professional email.

Return ONLY valid JSON.

Example:

{{
    "subject": "Work From Home Tomorrow",
    "body": "Dear Team,\\n\\nTomorrow will be Work From Home. Please work remotely.\\n\\nRegards"
}}

Instruction:
{instruction}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        return json.loads(response.text)