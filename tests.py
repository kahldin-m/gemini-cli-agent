# tests.py
# Will run the following function calls on the get_files_info function
from functions.get_files_info import get_files_info


def main():
    test_args = [
        ("calculator", ".", "current"),  # Should list contents of current directory
        ("calculator", "pkg", "pkg"),  # Should list contents of pkg directory
        ("calculator", "/bin", "/bin"),  # Should return error message
        ("calculator", "../", "../"),  # Should return error message
    ]

    for wd, d, label in test_args:
        print(f"Result for '{label}' directory:")
        test = get_files_info(wd, d)
        print(test)


if __name__ == "__main__":
    main()