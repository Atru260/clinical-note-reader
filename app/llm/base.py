from abc import ABC, abstractmethod
from app.schemas import AnalysisResponse

class LLMClient(ABC):

    @abstractmethod
    def analyze(self, text: str) -> AnalysisResponse:
        """Analyze clinical text."""
        pass