# get_files_info.py
import os
import sys

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    working_directory = os.path.abspath(working_directory)
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    if not os.path.abspath(full_path).startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    """working_directory is the base. directory is the relative path from working_directory.full_path is the "target"... if full_path is outside working_directory: error"""

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    splay_dir = os.listdir(working_directory)
    print(f"Debug: splay_dir = {splay_dir}")
    for item in splay_dir:
        full_name = os.path.join(".", item)
        if os.path.isfile(full_name):
            print(f"- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_files_info.py <working_directory> <directory>")
        print('Example: python get_files_info.py "calculator" "."')
        sys.exit(1)
    result = get_files_info(sys.argv[1], sys.argv[2])
    print(result)
