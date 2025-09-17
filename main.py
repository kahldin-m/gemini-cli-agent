# main.py
import os
import sys
import call_function # type: ignore
from functions.config import system_prompt # type: ignore
from functions.get_files_info import schema_get_files_info, available_functions # type: ignore
from google import genai
from google.genai import types # type: ignore
from dotenv import load_dotenv # type: ignore

def main():
    load_dotenv()

    args = sys.argv[1:]
    if not args:
        print("Error: Please provide a prompt for the ai agent.")
        print('Usage: python main.py "<prompt>" --verbose (optional verbose flag)')
        print('Example: python main.py "Tell me a fact about beavers" --verbose')
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        )
    )
    if response.function_calls:
        for i, call in enumerate(response.function_calls, start=1):
            # print(f"Call function #{i}: {call.name}({call.args})")
            call_result = call_function.call_function(call, verbose="--verbose" in args)

            call_response = call_result.parts[0].function_response.response
            if not call_response:
                raise Exception("Fatal exception: No response from function call.")
            else:
                if "--verbose" in args:
                    print(f"-> {call_response}")
                else:
                    print(f"{call_response['result']}")
    else:
        print(response.text)
    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
