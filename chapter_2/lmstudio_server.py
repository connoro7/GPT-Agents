from openai import OpenAI
import requests

LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

# Point to the local server
client = OpenAI(base_url=LM_STUDIO_BASE_URL, api_key="not-needed")

try:
    models = requests.get(f"{LM_STUDIO_BASE_URL}/models").json()["data"]
except requests.exceptions.HTTPError:
    print("Could not get models. Is LM Studio server running?")
    raise

print("Available models:")
for model in [model["id"] for model in models]:
    print(model)

completion = client.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {
            "role": "system",
            "content": "You are an evil demon from the depths of hell. You are also a comedian that works at a night club on Wednesdays and Sundays, in order to help pay your rent. Sheparding souls to the underworld doesn't pay very well.",
        },
        {
            "role": "user",
            "content": "'Hi, I'm lost, can you help me?' *pulls out ancient ceremonial blade, forged by the sacred Elder One, blessed by His Name, crafted to rend demon flesh from demon bone*.",
        },
    ],
    temperature=0.9,
)
print(completion.choices[0].message.content)
# entrgrep lmstudio_server.py "uv run lmstudio_server.py"
