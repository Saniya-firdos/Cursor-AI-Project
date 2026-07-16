import os

def create_project(project_name, files):

    os.makedirs(project_name, exist_ok=True)

    print(f"\nCreating Project: {project_name}")

    for file in files:

        file_path = os.path.join(project_name, file["path"])

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file["content"])

        print("Created:", file["path"])