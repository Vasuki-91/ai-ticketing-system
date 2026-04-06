from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

# --- AI ANALYSIS FUNCTION ---
def analyze_ticket(question):
    q = question.lower()

    if "login" in q or "bug" in q:
        return {
            "category": "Bug",
            "summary": "Login issue detected",
            "severity": "High",
            "sentiment": "Frustrated",
            "action": "Assign",
            "department": "Engineering",
            "confidence": "90%"
        }

    elif "leave" in q or "salary" in q:
        return {
            "category": "HR",
            "summary": "HR related query",
            "severity": "Low",
            "sentiment": "Polite",
            "action": "Auto-resolve",
            "department": "HR",
            "confidence": "95%"
        }

    else:
        return {
            "category": "Other",
            "summary": "General request",
            "severity": "Medium",
            "sentiment": "Neutral",
            "action": "Auto-resolve",
            "department": "Support",
            "confidence": "80%"
        }

# --- AUTO RESPONSE ---
def auto_response(category):
    if category == "HR":
        return "You can apply leave through HR portal."
    return "Your query has been resolved."

# --- API ---
@app.post("/ask")
def ask(query: Query):
    q = query.question.lower()

    if "login" in q:
        answer = "Please reset your password or check your credentials."
        category = "Authentication"
        department = "IT Support"

    elif "payment" in q:
        answer = "Please verify your payment details or contact billing support."
        category = "Billing"
        department = "Finance"

    elif "error" in q:
        answer = "Try restarting the system or clearing cache."
        category = "Technical"
        department = "Tech Team"

    else:
        answer = "Your query has been resolved."
        category = "Other"
        department = "Support"

    return {
        "answer": answer,
        "analysis": {
            "category": category,
            "summary": query.question,
            "severity": "Medium",
            "sentiment": "Neutral",
            "action": "Auto-resolve",
            "department": department,
            "confidence": "80%"
        }
    }