from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.document_loaders import PyPDFLoader
from google.adk import Agent, Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService

from jinja2 import Environment, FileSystemLoader
def render_pdf_prompt():
    """Renders a PDF prompt using Jinja2 template."""
    # Set up Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('question_generator_agent/pdf_prompt.j2')
    # Render the template with variables
    return template.render()

async def create_pdf_loader(file_path: str):
    """Asynchronously loads a PDF file and extracts its pages. It returns a list of pages."""
    # Initialize PDF loader with the provided file path
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

prompt = render_pdf_prompt()

root_agent = Agent(
    name="PDF_reader_agent",
    description="Root agent that manages PDF reading tasks.",
    tools=[create_pdf_loader],
    model="gemini-2.0-flash",
    instruction=prompt,
    # session_service=InMemorySessionService()
)
