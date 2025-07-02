from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.document_loaders import PyPDFLoader
from google.adk import Agent, Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
import asyncio
from langchain_unstructured import UnstructuredLoader

from jinja2 import Environment, FileSystemLoader
def render_pdf_prompt():
    """Renders a PDF prompt using Jinja2 template."""
    # Set up Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('url_question_generator/url_prompt.j2')
    # Render the template with variables
    return template.render()

async def create_url_loader(web_url: str):
    """Asynchronously loads a web page and extracts its content. It returns a list of documents."""
    # Initialize UnstructuredLoader with the provided web URL
    loader = UnstructuredLoader(web_url=web_url)
    docs = []
    async for doc in loader.alazy_load():
        docs.append(doc)
    return docs

async def fetch_page(page_url: str):
    """Asynchronously fetches a web page and extracts its content."""
    # Call the create_url_loader function to load the web page
    docs = await create_url_loader(page_url)
    for doc in docs:
        print(doc.page_content)
    return docs

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