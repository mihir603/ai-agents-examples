from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

if not api_key:
  raise ValueError("No API key found")
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=api_key)

def ask_gemini(query):
  response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
      {"role" : "system", "content" : "You are a helpful assistant."},
      {"role" : "user", "content" : query}
    ]
  )
  return response.choices[0].message.content

query = "What is Capital of India?"
print(ask_gemini(query))

