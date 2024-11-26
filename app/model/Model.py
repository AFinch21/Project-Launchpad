from pydantic import BaseModel

class AgentDetails(BaseModel):
    id: int
    agent_name: str
    system_prompt: str
    user_prompt: str
    
class TaskManagerClassification(BaseModel):
    category: str