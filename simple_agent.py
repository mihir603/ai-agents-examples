from agents import Agent, Runner, ModelSettings
from dotenv import load_dotenv

load_dotenv()

instructions = """ 
You are a travel planning agent.

**Task Instructions**
- You will be given a Trip Destination.
- Your task is to provide a good plan for things to do and places to visit there.
- Output 5 tasks (10 words or less) to your plan. 
"""

# agent = Agent(name="Travel Planner", 
#               instructions=instructions)
agent = Agent(name="Travel Planner",
              instructions=instructions,
              model="gpt-4.1",
              model_settings=ModelSettings(
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.5,
              )
              )

query = "Singapore Trip for 3 days."

result = Runner.run_sync(agent, input=query)

print(result)


