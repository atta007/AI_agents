from xai_sdk import Client
from xai_sdk.chat import user, system
from config import GROK_API_KEY
client = Client(api_key=GROK_API_KEY, timeout=3600)

def get_chat_response(system_prompt: str, message: str, history: list) -> str:
    chat_session = client.chat.create(model="grok-3", messages=[system(system_prompt)])

    for user_msg, assistant_msg in history:
        chat_session.append(user(user_msg))
        chat_session.append(system(assistant_msg))

    chat_session.append(user(message))
    response = chat_session.sample()
    return response.content
