from fastapi import FastAPI, Request, Response
import uvicorn
from utils import send_chat_to_chatwoot

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request, token) -> Response:
    body = await request.json()
    message = body.get("content")

    if message == 'Hi':
        account_id = body.get("account")['id']
        conversation_id = body.get("conversation")['id']
        data = {"content": f"Hello. Conversation: {conversation_id}"}
        
        response = send_chat_to_chatwoot(account_id=account_id, conversation_id=conversation_id, data=data)
        
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=3002, reload=True)