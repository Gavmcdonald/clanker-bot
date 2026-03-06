import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
    
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,file_path))   
        valid_dir = os.path.commonpath([path,target_dir]) == path
    
        if not valid_dir:
            return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file = open(target_dir)
        contents = file.read(10000)
        
        if file.read(1):
            contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return contents

    except OSError as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
name="get_file_content",
description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "directory": types.Schema(
            type=types.Type.STRING,
            description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
        ),
    },
),)



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)