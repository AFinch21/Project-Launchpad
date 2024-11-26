from fastapi import FastAPI
from pathlib import Path
from utilities.AgentArchetype import Agent, TaskManager
import os

app = FastAPI()

@app.get("/createagent")
async def create_agent(agent_name: str):
    print(os.environ.get('OPEN_AI_API_KEY'))
    agent = TaskManager(
        agent_id = 'test',
        agent_name= agent_name,
        api_key = os.environ.get('OPEN_AI_API_KEY')
    )
    
    print(agent.agent_name)
    print(agent.agent_id)
    print(agent.get_response(agent_name))
