from .base import LLMClient
from google import genai
import os
from dotenv import load_dotenv

class GeminiClient(LLMClient):
    
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL_NAME")
        self.prompt = "Return the symptoms in this note: "

    def analyze(self, text):
        interaction = self.client.interactions.create(
            model=self.model,
            input=self.prompt + text
        )

        return interaction.output_text