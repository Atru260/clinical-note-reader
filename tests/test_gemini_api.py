import os

from dotenv import load_dotenv
from google import genai


'''
Isolate gemini api from analyze call
'''
def test_gemini_api():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    model= os.getenv("GEMINI_MODEL_NAME")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing from the .env file.")

    client = genai.Client(api_key=api_key)

    interaction = client.interactions.create(
        model=model,
        input="Return the names of the symptoms in this note: Patient has headache and nausea.",
        store=False,
    )
    print(interaction.output_text)