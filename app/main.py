from fastapi import FastAPI
from pathlib import Path
from utilities.AgentArchetype import Agent
import os

app = FastAPI()

@app.get("/createagent")
async def create_agent(agent_name: str):
    print(os.environ.get('OPEN_AI_API_KEY'))
    agent = Agent(
        agent_id = 'test',
        agent_name= ' test_name',
        api_key = os.environ.get('OPEN_AI_API_KEY')
    )
    
    print(agent.agent_name)
    print(agent.agent_id)
    print(agent.get_llm_response("Hello"))
