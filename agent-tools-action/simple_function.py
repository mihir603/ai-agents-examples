import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')
if not api_key:
  raise ValueError("No API key found....")

client = OpenAI(api_key=api_key)


def ask_chatgpt(user_msg):
  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role" : "system", "content" : "You are a helpful assistant."},
              {"role": "user", "content": user_msg}],
    temperature=0.7,
    tools=[
      {
              "type": "function",
                "function": {
                    "name": "recommend",
                    "description": "Provide a recommendation for any topic.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "The topic, a user wants a recommnedation for.",
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
  )
  return response.choices[0].message.tool_calls[0].function


# query = "Can you please recommend me some good places to go for vacation this holiday season?"
# answer = ask_chatgpt(query)

# print(answer)


query = "Can you please recommend me some places to go for vacation this holiday season?"
answer = ask_chatgpt(query)

print(answer)
