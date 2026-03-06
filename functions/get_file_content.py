import os
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