from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class AgentDetails:
    id: int
    agent_name: str
    system_prompt: str
    user_prompt: str
