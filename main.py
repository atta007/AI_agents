import gradio as gr
from config import LINKEDIN_PDF_PATH, SUMMARY_FILE_PATH, NAME
from utils.pdf_utils import extract_text_from_pdf
from utils.text_utils import read_text_file
from utils.prompt_utils import build_system_prompt
from services.chat_service import get_chat_response


linkedin_text = extract_text_from_pdf(LINKEDIN_PDF_PATH)
summary_text = read_text_file(SUMMARY_FILE_PATH)
system_prompt = build_system_prompt(NAME, summary_text, linkedin_text)


def chat_interface(message: str, history: list) -> str:
    return get_chat_response(system_prompt, message, history)

if __name__ == "__main__":
    gr.ChatInterface(chat_interface).launch()
