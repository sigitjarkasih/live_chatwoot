from requests import Response, post
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def send_chat_to_chatwoot(account_id: int, conversation_id: int, data: any) -> Response:
    api_access_token = getenv("API_ACCESS_KEY")
    base_url = getenv("API_BASE_URL")
    url = f"{base_url}/accounts/{account_id}/conversations/{conversation_id}/messages"
    headers = {"api_access_token": api_access_token}
    
    return post(url=url, json=data, headers=headers)