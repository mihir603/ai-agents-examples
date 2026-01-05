from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

if not api_key:
  raise ValueError("No API Key Found.")
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=api_key)

def ask_gemini(messages):
  response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages,
    temperature=0.6,
    response_format={"type": "json_object"}
  )
  return response.choices[0].message.content

messages = [
  {"role" : "system", "content" : "You are a helpful assistant, always output JSON."},
  {"role" : "user", "content" : "Tell me who's the best driver in Formula-1"},
  {"role" : "assistant", "content" : "The best driver in Formula-1 is Lewis Hamilton"},
  {"role": "user", "content": "What was the best race of Lewis Hamilton"}
]
response = ask_gemini(messages)
with open("json_output.txt", "w") as f:
  f.write(response)
f.close()
 
