# tests.py
# Will run the following function calls on the get_files_info function
from functions.get_files_info import get_files_info


def main():
    # Test 1
    # This should list the contents of the current directory
    get_files_info("calculator", ".")
    # Test 2
    # This should list the contents of the pkg directory
    get_files_info("calculator", "pkg")
    # Test 3
    # This should return an error message
    get_files_info("calculator", "/bin")
    # Test 4
    # This should return an error message
    get_files_info("calculator", "../")


if __name__ == "__main__":
    main()