from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from typing import List

Base = declarative_base()

class Agent(Base):
    __tablename__ = "agents"
    
    agent_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    agent_name: Mapped[str] = mapped_column(String)
    system_prompt: Mapped[str] = mapped_column(String)
    user_prompt: Mapped[str] = mapped_column(String)

    # Correctly annotated relationship with Mapped
    requests: Mapped[List['UserRequest']] = relationship("UserRequest", back_populates="agent")

    def __repr__(self) -> str:
        return f"Agent(agent_id={self.agent_id!r}, agent_name={self.agent_name!r}, system_prompt={self.system_prompt!r}, user_prompt={self.user_prompt!r})"

class UserRequest(Base):
    __tablename__ = "user_requests"
    
    request_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    agent_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('agents.agent_id'))
    user_input: Mapped[str] = mapped_column(String)

    # Relationship to Agent
    agent: Mapped[Agent] = relationship("Agent", back_populates="requests")

    def __repr__(self) -> str:
        return f"UserRequest(request_id={self.request_id!r}, agent_id={self.agent_id!r}, user_input={self.user_input!r})"