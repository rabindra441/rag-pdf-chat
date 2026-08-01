from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

messages = []

while True:
    msg = input("You: ")
    if msg.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": msg})

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content":
                   msg}]
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant",
                     "content": reply})

    print(f"Bot: {reply}\n")