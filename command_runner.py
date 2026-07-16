import subprocess
import time

def run_commands(commands, project_name):

    print("\nExecuting Commands...\n")

    for command in commands:

        print(f"Executing: {command}")

        subprocess.Popen(
            command,
            shell=True,
            cwd=project_name
        )

    time.sleep(2)