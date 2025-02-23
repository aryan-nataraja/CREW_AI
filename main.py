from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPEnAI_MODEL_NAME"] = "gpt-4" 

rules_agent = Agent(
    role="Rules Agent",
    goal="Give structured rules for any sport or board game. The rules should be easy to understand",
    backstory="""
        You love spots, board games and video games. Everyone always comes to you if they are confused about the rules or need clarification. 
        You are an expert at this.
    """
)

task1 = Task(
    description="Tell me the rules to the Italian game Scopa",
    expected_output="Give a quick summary of the game and then a step by step guide on how to play the game",
    agent=rules_agent
)

crew = Crew(
    agents=[rules_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print("################")
print(result)
