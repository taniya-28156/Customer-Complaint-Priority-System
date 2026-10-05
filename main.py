from fastapi import FastAPI
from pydantic import BaseModel

from ml_utils import predict_domain, predict_category, predict_category_confidence, predict_priority
# from smart_ai import generate_ai_response
from ai_utils import generate_ai_response

app = FastAPI()
class ComplaintRequest(BaseModel):
    complaint: str

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Customer Complaint System"
    }

@app.post("/predict")
def predict(request: ComplaintRequest):

    domain = predict_domain(request.complaint)
    category = predict_category(request.complaint)
    priority = predict_priority(request.complaint)
    confidence = predict_category_confidence(request.complaint)

    try:
        ai_response = generate_ai_response(
            request.complaint,
            domain,
            category,
            priority
        )
    except Exception:
        ai_response = "AI service is temporarily unavailable. Please try again later."

    return {
        "domain": domain,
        "category": category,
        "confidence": confidence,
        "priority": priority,
        "ai_response": ai_response
    }