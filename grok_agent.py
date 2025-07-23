from dotenv import load_dotenv
from pypdf import PdfReader
import gradio as gr
from xai_sdk import Client
from xai_sdk.chat import user, system
import os


load_dotenv(override=True)
client = Client(api_key=os.getenv('GROK_API_KEY'), timeout=3600)
LINKEDIN_PDF_PATH= "assets/linkedin.pdf"
NAME = "Ed Donner"
SUMMARY_FILE_PATH = "assets/summary.txt"

def extract_linkedin_text(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The text extracted from the PDF file.
    """

    reader = PdfReader(file_path)
    linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text
    return linkedin


def extract_summary_text(file_path: str) -> str:
    """
    Extracts text from a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The text extracted from the text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def build_system_prompt(name: str, summary: str, linkedin_profile: str) -> str:
    """Constructs the system prompt with profile context."""
    prompt = (
        f"You are acting as {name}. You are answering questions on {name}'s website, "
        f"particularly questions related to {name}'s career, background, skills, and experience. "
        f"Your responsibility is to represent {name} for interactions on the website as faithfully as possible. "
        f"You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. "
        f"Be professional and engaging, as if talking to a potential client or future employer who came across the website. "
        f"If you don't know the answer, say so.\n\n"
        f"## Summary:\n{summary}\n\n"
        f"## LinkedIn Profile:\n{linkedin_profile}\n\n"
        f"With this context, please chat with the user, always staying in character as {name}."
    )
    return prompt


linkedin_text = extract_linkedin_text(LINKEDIN_PDF_PATH)
summary_text = extract_summary_text(SUMMARY_FILE_PATH)
system_prompt = build_system_prompt(NAME, summary_text, linkedin_text)


def chat_interface(message: str, history: list) -> str:
    """Handles conversation flow between user and the AI agent."""
    chat_session = client.chat.create(model="grok-3", messages=[system(system_prompt)])

    for user_msg, assistant_msg in history:
        chat_session.append(user(user_msg))
        chat_session.append(system(assistant_msg))

    chat_session.append(user(message))
    response = chat_session.sample()
    
    return response.content



gr.ChatInterface(chat_interface).launch()
