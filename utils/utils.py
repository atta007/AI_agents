from pypdf import PdfReader 
from dotenv import load_dotenv
from pypdf import PdfReader
import requests
import gradio as gr
from xai_sdk import Client
from xai_sdk.chat import user, system
from prompts.prompts import system_prompt
import os 





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





def chat_interface(message: str, history: list) -> str:
    """Handles conversation flow between user and the AI agent."""
    
    prompt_text = system_prompt(NAME, summary_text, linkedin_text)  # This is a string now

    chat_session = client.chat.create(model="grok-3", messages=[system(system_prompt)])

    for user_msg, assistant_msg in history:
        chat_session.append(user(user_msg))
        chat_session.append(system(assistant_msg))

    chat_session.append(user(message))
    response = chat_session.sample()
    
    return response.content        