from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.document_loaders import PyPDFLoader
from google.adk import Agent, Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
import asyncio

async def create_pdf_loader(file_path: str):
    """Asynchronously loads a PDF file and extracts its pages. It returns a list of pages."""
    # Initialize PDF loader with the provided file path
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages


root_agent = LlmAgent(
    name="PDF_reader_agent",
    description="Root agent that manages PDF reading tasks.",
    tools=[create_pdf_loader],
    model="gemini-2.0-flash",
    instruction="I can manage PDF reading tasks. Provide the file path to read the PDF file. The pdf file is one with python interview questions.",
    session_service=InMemorySessionService()
)
