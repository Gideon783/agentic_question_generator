from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.document_loaders import PyPDFLoader
from google.adk import Agent, Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
import asyncio
from langchain_unstructured import UnstructuredLoader
import sys
import os   
from dotenv import load_dotenv  
from .test import playwright_loader, fetch_page

load_dotenv()

from jinja2 import Environment, FileSystemLoader
def render_pdf_prompt():
    """Renders a PDF prompt using Jinja2 template."""
    # Set up Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('url_question_generator/url_prompt.j2')
    # Render the template with variables
    return template.render()

prompt = render_pdf_prompt()

root_agent = LlmAgent(
    name="URL_reader_agent",
    description="Root agent that manages URL reading tasks.",
    tools=[fetch_page],
    model="gemini-2.0-flash",
    # instruction="You are a helpful assistant that reads web pages and extracts their content but need to be provided with a URL. " \
    # "When a url is provided, you will read the page and return its content using the fetch_page tool whchich is an asynchronous function that loads the web page and extracts its content.",
    instruction=prompt,
    # session_service=InMemorySessionService()
)