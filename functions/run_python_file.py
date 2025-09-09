# run_python_file.py
import os
import sys
from subprocess import run

def run_python_file(working_directory, file_path, args=None):
    """
    Runs a Python file located at file_path within the specified working_directory.
    Args:
        working_directory (str): The directory in which to run the Python file.
        file_path (str): The path to the Python file to be executed, relative to working_directory.
        args (list): A list of arguments to pass to the Python file.
    Returns:
        str: The standard output and standard error from executing the Python file, or an error message.
    """
    # Avoid mutable default args
    if args is None:
        args = []

    # Normalize paths
    target_path = os.path.join(working_directory, file_path)
    working_directory = os.path.abspath(working_directory)
    target_path = os.path.abspath(target_path)

    # Security checks: Ensure the target path is within the working directory, exists and is a Python file
    if not target_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    if not target_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    # Security checks done

    # Execute the Python file
    try:
        executed_code = run(
            [sys.executable, file_path, *args], # Using sys.executable for portability
            cwd=working_directory,
            timeout=30,
            capture_output=True,
        )
        if executed_code.returncode != 0:
            return f'Error: Process exited with code {executed_code.returncode}'
        if executed_code.stdout == b'' and executed_code.stderr == b'':
            return "No output produced."
        
        output = f"STDOUT:\n{executed_code.stdout.decode("utf-8")}STDERR: {executed_code.stderr.decode("utf-8")}\n"
        return output
    
    except Exception as e:
        return f'Error: executing Python file: {e}'

## main for singular testing
# if __name__ == "__main__":
#     output = run_python_file("calculator", "main.py")
#     print(output)
