from schemas import AnalysisResponse, ExtractedClinicalData
from .base import LLMClient
from google import genai
import os
from dotenv import load_dotenv

class GeminiClient(LLMClient):
    
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL_NAME")
        self.prompt = '''Extract the clinical information contained in the note.
                    Rules:
                    - Only extract information supported by the note.
                    - Do not invent missing information.
                    - Do not make diagnoses.
                    - Preserve uncertainty.
                    Clinical note: '''

    def analyze(self, text):
        interaction = self.client.interactions.create(
            model=self.model,
            input=self.prompt + text,
            response_format=ExtractedClinicalData.model_json_schema()
        )

        return ExtractedClinicalData.model_validate_json(
            interaction.output_text
        )