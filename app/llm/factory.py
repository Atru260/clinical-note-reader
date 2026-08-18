import os
from dotenv import load_dotenv

from llm.gemini_client import GeminiClient
from llm.openai_client import OpenAIClient

# Provide a client based on provider in environment variable
def get_llm_client():
    load_dotenv()

    provider = os.getenv("Provider")

    if provider == "gemini":
        return GeminiClient()

    if provider == "gpt":
        return OpenAIClient()

    return None