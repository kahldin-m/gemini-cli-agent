# call_function.py
import sys
from google.genai import types # type: ignore
from functions.get_file_content import get_file_content  # type: ignore
from functions.get_files_info import get_files_info  # type: ignore
from functions.run_python_file import run_python_file  # type: ignore
from functions.write_file import write_file  # type: ignore

def call_function(function_call_part, verbose=False):
    """
    Handles the abstract task of calling a function based on the function call part provided by the AI model.
    Args:
        function_call_part (types.Part): The part containing the function call details.
        verbose (bool): If True, prints detailed information about the function call.
    Returns:
        types.Content: The content containing the function call result or error message.
"""

    function_name = function_call_part.name
    function_args = function_call_part.args

    function_args["working_directory"] = "./calculator"

    FUNCTIONS = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if not function_call_part.name in FUNCTIONS:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Call the function and get the result
    function_result = FUNCTIONS[function_name](**function_args)

    if verbose:
        print(f"Calling function: {function_name}({function_args})")

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
