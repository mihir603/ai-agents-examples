from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")
if not api_key:
  raise ValueError("No API Key Found.")

def prompt_llm(messages):
  client = OpenAI(base_url=base_url, api_key=api_key)
  response = client.chat.completions.create(
    messages=messages,
    model= model,
    temperature=0.7
  )
  return response.choices[0].message.content