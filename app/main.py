from fastapi import FastAPI
from pathlib import Path
from database.engine import get_db
from database.operations import get_agents, get_prompts
from utilities.AgentArchetype import Agent
from utilities.AgentInitialisation import iniatialise_agents
import os

app = FastAPI()

db = get_db()

agent_data = get_agents(db)

agent_pod = iniatialise_agents(agent_data)

print(agent_pod)
print(agent_pod[0].agent_name)
print(agent_pod[0].system_prompt)
print(agent_pod[1].agent_name)
print(agent_pod[1].system_prompt)



@app.get("/createagent")
async def create_agent(agent_name: str):
    pass
    
@app.get("/execute_task")
async def execute_task(user_input: str):
    
    pass