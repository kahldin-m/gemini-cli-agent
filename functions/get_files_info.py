# get_files_info.py
import os
import sys

"""
The directory parameter should be treated as a relative path within the working_directory. Use os.path.join(working_directory, directory) to create the full path, then validate it stays within the working directory boundaries.
"""

def get_files_info(working_directory, directory="."):
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    if not os.path.abspath(working_directory) == os.path.abspath(os.path.join(working_directory, directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    splay_dir = os.listdir(directory)
    for item in splay_dir:
        if os.path.isdir(item):
            print(f"- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_files_info.py <working_directory> <directory>")
        sys.exit(1)
    get_files_info(sys.argv[1], sys.argv[2])