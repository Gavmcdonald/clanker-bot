import os
from google.genai import types


def write_files(working_directory, file_path, content):
    try:
    
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,file_path))   
        valid_dir = os.path.commonpath([path,target_dir]) == path
    
        if not valid_dir:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_dir),exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


       
    except OSError as e:
        return f"Error: {e}"

    
schema_write_file = types.FunctionDeclaration(
    name="write_files",
    description="Writes text content to a specified file within the working directory (overwriting if the file exists)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)