# Kisumu Pharmacy Chatbot

A command-line assistant for pharmacy staff to answer common questions about
Kisumu Pharmacy's hours, services, medication availability, and prescriptions.
It sends the conversation history with each request so follow-up questions can
refer to earlier messages.

## Opening hours

- Monday to Saturday: 8:00 am–8:00 pm
- Sunday: 10:00 am–4:00 pm

## Services

- Prescription dispensing
- Repeat prescription refills
- Medication availability checks
- Over-the-counter medicine recommendations
- Pharmacist medication counseling
- Blood pressure checks
- Basic first-aid and health supplies

## Requirements

- Python 3
- An Anthropic API key

Install the required packages:

```bash
python -m pip install anthropic python-dotenv
```

## Configuration

Create a `.env` file in the project directory and add your API key:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Keep the `.env` file private; do not commit it to source control.

## Run

From the project directory:

```bash
python Day13_exercise.py
```

Enter questions at the `You:` prompt. Type `exit` to end the session.

## Safety notes

The assistant does not confirm medication stock unless staff has verified it,
does not promise prescription processing times, and refers clinical questions
to a pharmacist. Staff should confirm prescription documentation requirements
and all medication availability with the pharmacy before advising customers.
