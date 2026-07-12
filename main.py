from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os
import json

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(
    api_key = os.getenv("GENAI_API_KEY")

)
prompt = input(" what do you want to build? \n>")

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = f"""
You are Cursor AI.

You are an expert Software Engineer.

Rules:
1. Never explain.
2. Never ask questions.
3. Return ONLY valid JSON.
4. Create the complete project.
5. Also return terminal commands required to run the project.

JSON Format:

{{
    "project_name":"",
    "files":[
        {{
            "path":"",
            "content":""
        }}
    ],
    "commands":[]
}}

User Request:
{prompt}
"""
)
text = response.text.replace("```json", "")
text = text.replace("```", "")
text = text.strip()
response_data = json.loads(text)

project_name = response_data["project_name"]
print(f"\ncreating project:{project_name}")

os.makedirs(project_name, exist_ok=True)
for file in response_data["files"]:
    file_path = os.path.join(project_name, file["path"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file["content"])

    print("created:", file["path"])

print("\n project created successfully!")
