import os
from dotenv import load_dotenv

load_dotenv(override=True)

GROK_API_KEY = os.getenv('GROK_API_KEY')
LINKEDIN_PDF_PATH = "assets/linkedin.pdf"
SUMMARY_FILE_PATH = "assets/summary.txt"
NAME = "Ed Donner"