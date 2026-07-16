from gemini_client import generate_project
from project_creator import create_project
from command_runner import run_commands
from preview import open_preview

prompt = input("What do you want to build?\n> ")

response = generate_project(prompt)

project_name = response["project_name"]
files = response["files"]
commands = response["commands"]
preview = response["preview"]

create_project(project_name, files)

run_commands(commands, project_name)

open_preview(project_name, preview)