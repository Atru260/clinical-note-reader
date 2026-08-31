from abc import ABC, abstractmethod
from schemas import AnalysisResponse, ExtractedClinicalData


class LLMClient(ABC):

    @abstractmethod
    def analyze(self, text: str) -> ExtractedClinicalData:
        """Analyze clinical text."""
        pass