import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
if OPENAI_MODEL is None:
    OPENAI_MODEL = ""


# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)


# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model=OPENAI_MODEL,  # gpt-4 turbo or a model of your preference
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


# Example usage
user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)
