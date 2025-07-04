import asyncio
import sys
import os   
from dotenv import load_dotenv  
load_dotenv()
from langchain_core.documents import Document
from playwright.async_api import async_playwright

async def playwright_loader(web_url: str):
    """Loads content from a webpage using Playwright."""
    """Asynchronously loads a web page and extracts its content. It returns a list of documents."""
    # Initialize UnstructuredLoader with the provided web URL
    docs = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(web_url)
        content = await page.content()
        text = await page.inner_text("body")  # Optional: scrape only visible text
        await browser.close()
        docs.append(Document(page_content=text, metadata={"source": web_url}))
    return docs

async def fetch_page(page_url: str):
    """Asynchronously fetches a web page and extracts its content."""
    # Call the playwright_loader function to load the web page
    docs = await playwright_loader(page_url)
    for doc in docs:
        print(doc.page_content[:1500]) #limit for pages too large
    return docs
