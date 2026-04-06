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
def ask_ai(query: Query):
    analysis = analyze_ticket(query.question)

    if analysis["action"] == "Auto-resolve":
        answer = auto_response(analysis["category"])
        return {
            "answer": answer,
            "analysis": analysis
        }
    else:
        ticket_id = f"TICK{random.randint(1000,9999)}"
        return {
            "answer": "Ticket assigned to department",
            "ticket_id": ticket_id,
            "analysis": analysis,
            "status": "Open",
            "category": "Bug",
            "severity": "High",
            "department": "Engineering",
            "sentiment": "Frustrated"
        }