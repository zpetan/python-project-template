"""Conditionals based on cookiecutter.json"""
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}


def remove(filepath):
    """Remove single file or folder and its content."""
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


REMOVE_VENV = "{{cookiecutter.create_local_folder_venv}}" != "y"

if REMOVE_VENV:
    # remove rel path to folder and all its content
    remove(os.path.join(os.getcwd(), ".venv"))
