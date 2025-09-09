# write_file.py
import os


def write_file(working_directory, file_path, content):
    target_path = os.path.join(working_directory, file_path)
    working_directory = os.path.abspath(working_directory)

    if not os.path.abspath(target_path).startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.abspath(file_path)):
        try:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            print("Created directories for path: ", os.path.dirname(target_path))
        except Exception as e:
            return f'Error: {e}'
    try:
        with open(target_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'