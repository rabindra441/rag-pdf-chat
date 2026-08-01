from groq import Groq
import json
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_weather(city):
    # Simulated weather data for demonstration purposes
    weather_data = {
        "kolkata": "The weather in Kolkata is currently sunny with a temperature of 30°C.",
        "new York": "The weather in New York is currently cloudy with a temperature of 22°C.",
        "london": "The weather in London is currently rainy with a temperature of 15°C."
    }
    return weather_data.get(city.lower(), "Weather data not available for this city.")
tools = [
    {"type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to get the weather for."
                    }
                },
                "required": ["city"]
            }
        }
    }
]


messages = [{"role":"user", "content":"What is the weather like in Kolkata right now?."}]
#
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice='auto'
)

response_message = response.choices[0].message
tool_call = response.choices[0].message.tool_calls[0]
args = json.loads(tool_call.function.arguments)

result = get_weather(args['city'])

messages.append(response_message)
messages.append({"role": "assistant",
                 "content": response_message.content,
                 "tool_calls":[
                     {
                      "id": tool_call.id,
                      "type": "function",
                      "function": {
                      "name": tool_call.function.name,
                      "arguments": tool_call.function.arguments
             }
        }
    ]
})
messages.append({
    "role": "function",
    "name": tool_call.function.name,
    "content": result})
final_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
)
print(final_response.choices[0].message.content)


# print("Function result:", result)