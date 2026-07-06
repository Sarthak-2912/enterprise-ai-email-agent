import json
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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

        response = client.chat.completions.create(
            model="qwen/qwen3-32b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)