import os

from dotenv import load_dotenv

from llm.gemini_client import GeminiClient


def test_gemini_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    client = GeminiClient(api_key=api_key)


    print(client.analyze("Patient has headache and nausea."))