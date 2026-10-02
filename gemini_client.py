from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os
import json

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(
    api_key=os.getenv("GENAI_API_KEY")
)

def generate_project(prompt):

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
You are Cursor AI.

You are an expert Software Engineer.

Rules:
1. Never explain.
2. Never ask questions.
3. Return ONLY valid JSON.
4. Create the complete project.
5. Also return terminal commands required to run the project.
6. Do not generate commands for creating folders or files.
7. Only generate commands required to install dependencies or run the project.
8. Return a preview path.

JSON Format:

{{
    "project_name":"",
    "files":[
        {{
            "path":"",
            "content":""
        }}
    ],
    "commands":[],
    "preview":""
}}

User Request:
{prompt}
"""
    )

    text = response.text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)
