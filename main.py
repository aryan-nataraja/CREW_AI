from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPEnAI_MODEL_NAME"] = "gpt-4" 
