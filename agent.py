import json
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

#Tool 1: Calculator
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

#Tool 2: Weather
def get_weather(city):
    weather_data = {
        "kolkata": "Sunny, 25°C",
        "delhi": "Hot and dry, 38°C",
        "mumbai": "Rainy, 18°C"
    }
    return weather_data.get(city.strip().lower(), "Weather data not available for this city")

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "A calculator that can evaluate mathematical expressions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate."
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

availabe_functions = {
    "calculator": calculator,
    "get_weather": get_weather
}

def run_agent(user_question):
    messages = [{"role": "system", "content": "You have access to tools that provide real, current data. When a tool returns a result, treat it as accurate and current, and use it directly in your answer without adding disclaimers about not having real-time access"},
                {"role":"user", "content":user_question}]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message

    # if the AI wants to call a tool
    if response_message.tool_calls:
       messages.append({
            "role": "assistant",
            "content": response_message.content,
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments}
                } for tc in response_message.tool_calls
            ]
        })
        # Run EVERY tool call the AI requested
    for tool_call in response_message.tool_calls:
            func_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            result = availabe_functions[func_name](**args)

            print(f"[Agent used tool:{func_name}({args}) -> {result}]")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })

    final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
    return final_response.choices[0].message.content

    return response_message.content

#Test it
print(run_agent("What's 25 times 4, and what's the weather in kolkata"))


        # Call the appropriate tool function
