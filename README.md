# Agentic Question Generator

This project is an agent-based Python application that generates interview questions from PDF files containing Python information. It leverages Google ADK, LangChain, and Jinja2 to extract content, generate prompts, and create dynamic interview questions and answers.

## Features
- **PDF Parsing:** Reads and extracts content from user-provided PDF files.
- **Dynamic Prompting:** Uses a Jinja2 template to generate system prompts for the LLM agent.
- **Customizable Questions:** Generates a default of 10 questions, or a user-specified number, focusing on user-listed skills if provided.
- **Agentic Architecture:** Modular agents for coordination, question generation, and PDF handling.
- **Environment Variable Support:** Loads API keys and settings from `.env` files.

## Project Structure
```
interviewer/
├── agent_file/
│   ├── coordinator_agent/
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── question_generator_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── pdf_prompt.j2
│   └── url_question_generator/
│       ├── __init__.py
│       └── agent.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Gideon783/agentic_question_generator.git
   cd agentic_question_generator
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv .interviewer
   .interviewer\Scripts\activate  # On Windows
   # Or: source .interviewer/bin/activate  # On Unix/Mac
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys (Google, Tavily, etc).
   - Example:
     ```env
     GOOGLE_GENAI_USE_VERTEXAI=FALSE
     GOOGLE_API_KEY=your_google_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

## Usage
- Place your PDF file in a known location.
- Run the main agent or use the provided scripts to generate questions:

```python
from agent_file.question_generator_agent.agent import root_agent

# Example: Generate questions from a PDF
result = await root_agent.run(file_path="path/to/your/python_info.pdf")
print(result)
```

- The agent will:
  - Parse the PDF
  - Render the system prompt using `pdf_prompt.j2`
  - Generate interview questions (and answers if available) based on the PDF and user-specified skills/number of questions

## Customization
- **Change the number of questions or required skills** by modifying the arguments to `render_pdf_prompt` in `agent.py`.
- **Edit the prompt template** in `agent_file/question_generator_agent/pdf_prompt.j2` for different instructions or output formats.

## Security
- **Never commit your `.env` or virtual environment folders.**
- The `.gitignore` is set up to prevent this, but always double-check before pushing.
- If you accidentally commit secrets, remove them from git history and rotate your keys immediately.

## License
MIT License

## Acknowledgements
- [Google ADK](https://github.com/google/adk)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Jinja2](https://palletsprojects.com/p/jinja/)
