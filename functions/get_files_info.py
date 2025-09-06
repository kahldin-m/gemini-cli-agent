# get_files_info.py
import os
import sys

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
    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_files_info.py <working_directory> <directory>")
        print('Example: python get_files_info.py "calculator" "."')
        sys.exit(1)
    result = get_files_info(sys.argv[1], sys.argv[2])
    print(result)
