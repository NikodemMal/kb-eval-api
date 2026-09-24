from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EvaluationRequest(BaseModel):
    question: str
    answer: str
    source: str


class EvaluationResult(BaseModel):
    accuracy: int
    hallucination: int
    reasoning: str

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.post("/evaluate", response_model=EvaluationResult)
def evaluate(request: EvaluationRequest):
    return EvaluationResult(
        accuracy=2,
        hallucination=0,
        reasoning="stub",
    )