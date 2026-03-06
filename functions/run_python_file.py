import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
    
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,file_path))   
        valid_dir = os.path.commonpath([path,target_dir]) == path
    
        if not valid_dir:
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args != None:
            command.extend(args)

        process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True,timeout=30)

        if process.returncode != 0:
            return f"Process exited with code {process.returncode}"
        elif process.stdout == None and process.stderr == None:
            return "No output produced"
        else:
            return f"STDOUT: {process.stdout}\n" + f"STDERR: {process.stderr}"
        
    except BaseException as e:
        return f"Error: {e}"

    
    