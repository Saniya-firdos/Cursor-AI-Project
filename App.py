import streamlit as st
from gemini_client import generate_project
from project_creator import create_project
from command_runner import run_commands

st.title("Cursor AI Project Generator")

prompt = st.text_area(
    "What do you want to build?",
    placeholder="Example: Create a Python calculator"
)

if st.button("Generate Project"):

    if not prompt.strip():
        st.warning("Please enter a project idea.")
    else:
        with st.spinner("Generating your project..."):

            try:
                response = generate_project(prompt)

                project_name = response["project_name"]
                files = response["files"]
                commands = response["commands"]

                create_project(project_name, files)

                run_commands(commands, project_name)

                st.success(f"Project '{project_name}' created successfully!")

                st.subheader("Generated Files")

                for file_name in files:
                    st.write(f"- {file_name}")

            except Exception as e:
                st.error(f"Error: {e}")