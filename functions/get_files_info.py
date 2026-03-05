import os

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
if __name__ == "__main__":
    get_files_info('../../calculator','../../../functions')
    
    