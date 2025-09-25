# main.py
import os
import sys
import call_function # type: ignore
from functions.config import system_prompt, MAX_GEN_CALL # type: ignore
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

    for n in range(MAX_GEN_CALL):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                )
            )

            # Check .candidates property so we can add it to our conversation history stored in messages
            if response.candidates:
                for candidate in response.candidates:
                    # Add the contents of each candidate to messages
                    messages.append(candidate.content)

            if response.function_calls:
                for i, call in enumerate(response.function_calls, start=1):
                    # Call the function and get the result
                    call_result = call_function.call_function(call, verbose="--verbose" in args)
                    call_response = call_result.parts[0].function_response.response
                    
                    if not call_response:
                        raise Exception("Fatal exception: No response from function call.")
                    else:
                        if "--verbose" in args:
                            preview = str(call_response.get("result", ""))[:50].replace("\n","\\n")
                            print(f" -> result: {preview}{'...' if len(str(call_response.get('result',''))) > 200 else ''}")
                        
                    # Convert the function response into a message with a role of 'user' and append to messages
                    user_msg = types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                function_response=types.FunctionResponse(
                                    name=call.name,  # the tool's name
                                    response=call_response   # the dict/payload returned by the tool
                                ),
                            )
                        ]
                            
                    )
                    messages.append(user_msg)
            # Check if the generate_content returned the response.text property. If so, it's done, so print the final response and break the loop.
            # Otherwise, iterate again (unless max iterations reached, of course)
            else:
                print("Final response:")
                print(response.text)
                break

        except Exception as e:
            return f"Error during generation or function call: {e}"
        
    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
