# get_files_info.py
import os
import sys
from google.genai import types # type: ignore

def get_files_info(working_directory, directory="."):
    """Lists files in a directory with their sizes and whether they are directories.
    Args:
        working_directory (str): The base directory to work within.
        directory (str): The target directory to list files from, relative to working_directory."""
    # working_directory is the base. directory is the relative path from working_directory.
    # full_path is the "target"... if full_path is outside working_directory: error"
    full_path = os.path.join(working_directory, directory)
    working_directory = os.path.abspath(working_directory)

    # If the absolute path to the directory is outside the working_directory, return a string error message:
    if not os.path.abspath(full_path).startswith(working_directory):
        return f'  Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'  Error: "{directory}" is not a directory'
    
    # Collect file info into a new list
    splay_dir = os.listdir(full_path)
    info_results = []
    try:
        with os.scandir(full_path) as entries:
            for entry in entries:
                try:
                    if entry.name in splay_dir:
                        info_results.append(f" - {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}")
                except Exception as e:
                    return f"Error: {e}"
            return "\n".join(info_results)
    except Exception as e:
        return f"Error: {e}"
    

# """Every schema follows this structure:

# schema_function_name = types.FunctionDeclaration(
#     name="function_name",  # Must match your actual function name
#     description="What this function does",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "param_name": types.Schema(
#                 type=types.Type.STRING,  # or INTEGER, BOOLEAN, etc.
#                 description="What this parameter is for",
#             ),
#         },
#         required=["param_name"],  # List of required parameters
#     ),
# )
# """


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file and returns its output, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="A list of arguments to pass to the Python file.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a text file, constrained to the working directory. If the file already exists, it will be overwritten.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory where the file is located, relative to the working directory. If not provided, lists files in working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

schema_summarize_file = types.FunctionDeclaration(
    name="summarize_file",
    description="Creates a brief natural-language summary of a text file's contents for a non-technical audience.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to summarize, relative to the working directory.",
            ),
            "max_sentences": types.Schema(
                type=types.Type.INTEGER,
                description="Maximum number of sentences in the summary. Defaults to 3 if not provided.",
            ),
        },
        required=["file_path"],
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
        schema_summarize_file,
    ]
)

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python get_files_info.py <working_directory> <directory>")
#         print('Example: python get_files_info.py "calculator" "."')
#         sys.exit(1)
#     result = get_files_info(sys.argv[1], sys.argv[2])
#     print(result)
