# get_file_content.py
import os
from sys import argv
from functions.config import MAX_CHARS # type: ignore

def get_file_content(working_directory, file_path):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory = os.path.abspath(working_directory)

    if not target_path.startswith(working_directory):
        return f'  Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path):
        return f'  Error: File not found or is not a regular file:  "{file_path}"'
    
    try:
        with open(target_path, "r") as f:
            try:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
                return file_content_string
            except Exception as e:
                return f"  Error: {e}"
    except Exception as e:
        return f"  Error: {e}"

# if __name__ == "__main__":
#     result = get_file_content(argv[1], argv[2])
#     print(result)
