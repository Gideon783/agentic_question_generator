from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.document_loaders import PyPDFLoader
from google.adk import Agent, Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv
import sys
import os

load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from question_generator_agent.agent import root_agent as question_generator_agent
from url_question_generator.agent import root_agent as url_question_generator_agent

from jinja2 import Environment, FileSystemLoader
def render_pdf_prompt():
    """Renders a PDF prompt using Jinja2 template."""
    # Set up Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('coordinator_agent/coordinator_prompt.j2')
    # Render the template with variables
    return template.render()

root_agent = Agent(
    name="Coordinator_agent",
    description="Root agent that coordinates between the pdf and url agents.",
    sub_agents=[question_generator_agent, url_question_generator_agent],
    model="gemini-2.0-flash",
    instruction=render_pdf_prompt(),
)