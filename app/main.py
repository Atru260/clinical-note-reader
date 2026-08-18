from fastapi import FastAPI
from pydantic import BaseModel
from services.analyzer import analyze_clinical_text
from schemas import AnalysisRequest
print("running")
app = FastAPI()

# Dummy
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

#TODO: add more info
@app.get("/health")
def health():
    return {"status": "ok"}

#TODO: Replace analyze function with llm_client's
@app.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_clinical_text(request.text)
