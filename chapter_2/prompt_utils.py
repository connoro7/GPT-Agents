from connecting import OPENAI_MODEL
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  # loading and setting the api key can be done in one step


# Example function to query ChatGPT
def prompt_llm(messages, model: str = "", base_url=None, api_key=""):
    if OPENAI_MODEL is None:
        raise ValueError(f"No model selected, {model=}")
    model = OPENAI_MODEL
    if base_url:
        # Azure or local LLM deployment
        client = OpenAI(base_url=base_url, api_key=api_key)
    else:
        # OpenAI deployment, api key set in environment variable
        client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content
