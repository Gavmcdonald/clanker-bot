import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
    
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,directory))   
        valid_dir = os.path.commonpath([path,target_dir]) == path
    
        if not valid_dir:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        
        folder_contents = ""
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            size = os.path.getsize(full_path)
            is_directory = os.path.isdir(full_path)
            folder_contents += f"- {item}: file_size={size} bytes, is_dir={is_directory}\n"
        
        return folder_contents
    except OSError as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)