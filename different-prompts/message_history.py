from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
if not api_key:
  raise ValueError("No api key found.")
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=api_key)

def ask_gemini(messages):
  response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages
  )
  response_model = response.model_dump()
  print(json.dumps(response_model, indent=4))
  return response.choices[0].message.content

messages=[
      {"role" : "system", "content" : "You are a helpful assistant."},
      {"role" : "user" , "content" : "What is capital of India?"},
      {"role" : "system", "content" : "The Capital Of India is New Delhi"},
      {"role" : "user" , "content" : "Tell me an interesting myth about New Delhi"}
    ]
response = ask_gemini(messages)
with open("./myth-output.txt", "w") as f:
  f.write(response)
f.close()