from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
conversation = [
        {"role":"system", "content":"You are a helpful assistant."}
    ]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=conversation
)
reply = response.choices[0].message.content
print("AI:", reply)

conversation.append({"role": "assistant", "content": reply})