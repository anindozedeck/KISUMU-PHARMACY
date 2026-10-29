import json
from datetime import datetime

import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system_prompt = """You are an assistant for Otieno Wholesale in Kisumu.
Answer questions about stock, pricing, and delivery.
All prices in KES. Be helpful and brief."""

messages = []
conversation_log = []
print("Otieno Wholesale Assistant. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)
    conversation_log.append(user_message)
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=system_prompt,
        messages=messages
    )
    
    reply = response.content[0].text
    assistant_message = {"role": "assistant", "content": reply}
    messages.append(assistant_message)
    conversation_log.append(assistant_message)
    if len(messages) > 10:
        messages = messages[-10:]
    print(f"Assistant: {reply}")

log = {
    "date": datetime.now().isoformat(),
    "messages": conversation_log
}
with open("chat_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)
print("Conversation saved to chat_log.json")