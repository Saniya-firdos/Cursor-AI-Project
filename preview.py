import os
import webbrowser

def open_preview(project_name, preview):

    print("\nOpening Preview...\n")

    if preview.startswith("http"):

        webbrowser.open(preview)

    else:

        preview_path = os.path.abspath(
            os.path.join(project_name, preview)
        )

        if os.path.exists(preview_path):

            webbrowser.open(preview_path)