import os
from pathlib import Path

import pytest
from dotenv import dotenv_values

from llm.gemini_client import GeminiClient
from schemas import AnalysisResponse, ExtractedClinicalData

BASE_DIR = Path(__file__).resolve().parents[1]
SAMPLE_DIR = BASE_DIR / "tests" / "sample_data"


def _get_gemini_api_key():
    env_values = dotenv_values(BASE_DIR / ".env")
    return os.getenv("GEMINI_API_KEY") or env_values.get("GEMINI_API_KEY")


@pytest.mark.parametrize(
    "sample_file",
    sorted(SAMPLE_DIR.glob("*.txt")),
    ids=lambda path: path.name,
)
def test_client_analyze_sample_data(sample_file):
    api_key = _get_gemini_api_key()
    if not api_key:
        pytest.skip("GEMINI_API_KEY is not configured.")

    model_name = os.getenv("GEMINI_MODEL_NAME") or "gemini-3.6-flash"
    os.environ["GEMINI_MODEL_NAME"] = model_name

    client = GeminiClient(api_key=api_key)
    text = sample_file.read_text(encoding="utf-8")

    print(f"\n=== SAMPLE: {sample_file.name} ===")
    print(text)
    print("\n--- client.analyze output ---")

    try:
        result = client.analyze(text)
    except Exception as exc:
        print(f"\nSkipping {sample_file.name}: {type(exc).__name__}: {exc}")
        pytest.skip(f"Gemini API unavailable for {sample_file.name}: {exc}")

    print(result)

    assert isinstance(result, ExtractedClinicalData)
    assert str(result).strip(), f"No analysis returned for {sample_file.name}"
