from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

instructions = """ 
You are a travel planning agent.

**Task Instructions**
- You will be given a Trip Destination.
- Your task is to provide a good plan for things to do and places to visit there.
- Output 5 tasks (10 words or less) to your plan. 
"""

agent = Agent(name="Travel Planner", 
              instructions=instructions)

query = "Singapore Trip for 3 days."

result = Runner.run_sync(agent, input=query)

print(result)


