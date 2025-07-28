import os 
import requests
from dotenv import load_dotenv

load_dotenv(override=True)  

# pushover_api_key = os.getenv('PUSHOVER_API_KEY')
# pushover_user_key = os.getenv('PUSHOVER_USER_KEY')
# pushover_url = f"https://api.pushover.net/1/messages.json"



def push(text):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )

def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}

def record_unknown_question(question):
    push(f"Recording {question}")
    return {"recorded": "ok"}