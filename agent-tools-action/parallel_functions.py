import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
if not api_key:
  raise ValueError("No API key found...")

client = OpenAI(api_key=api_key)

def recommend(climate, rating="good"):
  """Giving Recommendation for any climate."""
  if "humid" in climate.lower():
    return json.dumps({
      "climate" : "humid",
      "recommendation" : "Malasiya",
      "rating" : rating
    })
  if "warm" in climate.lower():
    return json.dumps({
      "climate": "warm",
      "recommendation" : "Dubai",
      "rating" : rating
    })
  if "cozy" in climate.lower():
    return json.dumps({
      "climate" : "cozy",
      "recommendation" : "Goa",
      "rating" : rating 
    })

def run_conversation():
  query = """
    Can you please make recommendation for the following:
    1.Warm
    2. Cozy
    3. Humid"""
  messages = [{"role" : "user", "content": query}]

  tools = [
    {
              "type": "function",
                "function": {
                    "name": "recommend",
                    "description": "Provide a recommendation for any climate.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "climate": {
                                "type": "string",
                                "description": "The climate, a user wants a recommnedation for.",
                            },
                            "rating": {
                                "type": "string",
                                "description": "The rating this recommendation was given.",
                                "enum": ["good", "bad", "terrible"]
                                },
                        },
                        "required": ["topic"],
                    },
                },
                }
  ]

  response = client.chat.completions.create(
    model = "gpt-3.5-turbo-1106",
    messages = messages,
    tools = tools,
    tool_choice = "auto")
  
  response_msg = response.choices[0].message
  tool_calls = response_msg.tool_calls

  if tool_calls:
    available_funcs = {
      "recommend" : recommend
    }
    messages.append(response_msg)

    for tool_call in tool_calls:
      func_name = tool_call.function.name
      function_to_call = available_funcs[func_name]
      function_args = json.loads(tool_call.function.arguments)
      function_response = function_to_call(
        climate = function_args.get("climate"),
        rating = function_args.get("rating")

      )

      messages.append({
        "tool_call_id" : tool_call.id,
        "role" : "tool",
        "name": func_name,
        "content": function_response,

      })

    second_resp = client.chat.completions.create(
        model = "gpt-5-nano",
        messages = messages
      )
    return second_resp.choices[0].message.content
  


with open("agent-output.txt", "w") as file:
  final_resp = run_conversation()
  file.write(final_resp)
  file.close()
print("Done with tool calling...")
