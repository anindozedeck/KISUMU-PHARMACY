import os

import anthropic
from dotenv import load_dotenv


load_dotenv()

SYSTEM_PROMPT = """You are the staff-facing assistant for Kisumu Pharmacy in Kisumu, Kenya.

Opening hours:
- Monday to Saturday: 8:00 am to 8:00 pm
- Sunday: 10:00 am to 4:00 pm

Services include:
- Prescription dispensing
- Repeat prescription refills
- Checking medication availability
- Over-the-counter medicine recommendations
- Pharmacist medication counseling
- Blood pressure checks
- Basic first-aid and health supplies

Answer staff questions clearly and consistently. Use the full conversation history
to understand follow-up questions. Prescription processing times vary depending
on the prescription and stock; do not promise a specific time. For repeat
prescriptions, advise customers to bring their previous prescription or refill
record and the medication packaging if available, and have staff confirm any
additional documents needed. Never claim a medicine is in stock unless staff
has confirmed it. Do not diagnose or recommend prescription-only treatment;
refer clinical questions to the pharmacist."""


def answer_message(client, messages, user_input):
    """Add a user message, request a contextual reply, and retain both turns."""
    messages.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply


def main():
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    messages = []
    print("Kisumu Pharmacy Assistant. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break

        reply = answer_message(client, messages, user_input)
        print(f"Assistant: {reply}")


if __name__ == "__main__":
    main()