# tests.py
# Will run the following function calls on the get_files_info function
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file # type: ignore
from functions.run_python_file import run_python_file

def main():
    info_test = [
        ("calculator", ".", "current"),  # Should list contents of current directory
        ("calculator", "pkg", "pkg"),  # Should list contents of pkg directory
        ("calculator", "/bin", "/bin"),  # Should return error string
        ("calculator", "../", "../"),  # Should return error string
    ]

    content_test = [
        ("calculator", "main.py"), # Should return content of main.py
        ("calculator", "pkg/calculator.py"), # Should return content of calculator.py
        ("calculator", "/bin/cat"),  # Should return error string
        ("calculator", "pkg/does_not_exist.py")  # Should return error string
    ]
    write_test = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]
    run_test = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py")
    ]

    test_count = 0

    ## Testing get_files_info
    # for wd, d, label in info_test:
    #     print(f"Result for '{label}' directory:")
    #     result = get_files_info(wd, d)
    #     print(result)

    ## Testing get_file_content
    # for wd, fp in content_test:
    #     test_count += 1
    #     print(f"Test # {test_count}")
    #     result = get_file_content(wd, fp)
    #     print(result)

    ## Testing write_file
    # for wd, fp, content in write_test:
    #     test_count += 1
    #     print(f'Test # {test_count}')
    #     result = write_file(wd, fp, content)
    #     print(result)

    ## Testing run_python_file
    for wd, fp, *args in run_test:
        test_count += 1
        print(f'Test # {test_count}')
        if args:
            result = run_python_file(wd, fp, *args[0])
        else:
            result = run_python_file(wd, fp)
        print(result)

if __name__ == "__main__":
    main()