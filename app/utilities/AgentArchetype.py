from openai import OpenAI
from model.Model import AgentDetails

class Agent:
    def __init__(self, agent_id, agent_name, api_key):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.api_key = api_key
        self.client = self.get_client()
        self.system_prompt = self.get_system_prompt()
        self.user_prompt = self.get_user_prompt()
        

    def get_system_prompt(self) :
        system_prompt = "You are a spotify controller agent. You take tasks from a user and execute those tasks"
        
        return system_prompt
    
    def get_user_prompt(self) :
        user_prompt = "User message is here: {user message}"
        
        return user_prompt
    
    def get_client(self):
        # Adjust the instantiation of OpenAI according to its expected constructor
        client = OpenAI(api_key=self.api_key)  # Example: passing the api_key as a keyword argument
        return client
    
    def get_agent_details(self):
        
        details = AgentDetails(
            id = self.agent_id,
            agent_name = self.agent_name,
            system_prompt = self.system_prompt,
            user_prompt = self.get_user_prompt
        )
        
        return details
        
    def get_llm_response(self, input):
        # Method logic goes here
        
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": self.system_prompt},
                {
                    "role": "user",
                    "content": input
                }
            ]
        )
        
        return completion