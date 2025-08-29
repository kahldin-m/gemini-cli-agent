import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv # type: ignore

def main():
    load_dotenv()

    args = sys.argv[1:]
    if not args:
        print("""Error: Please provide a prompt for the ai agent.
Usage: main.py "Tell me a joke about cats."
Include an optional --verbose tag for further response data. ex.: main.py "Prompt here" --verbose""")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    print(response.text)
    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
