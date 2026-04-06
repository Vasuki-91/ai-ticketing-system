from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Ticket(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/analyze")
def analyze(ticket: Ticket):

    text = ticket.text.lower()

    if "password" in text:
        return {
            "category": "Access",
            "summary": "Password reset issue",
            "severity": "Low",
            "resolution": "auto",
            "department": "IT",
            "auto_response": "Please reset your password."
        }

    elif "server" in text:
        return {
            "category": "Server",
            "summary": "Server problem",
            "severity": "High",
            "resolution": "assign",
            "department": "Engineering",
            "auto_response": "Assigned to engineering team."
        }

    elif "salary" in text:
        return {
            "category": "Finance",
            "summary": "Salary issue",
            "severity": "Medium",
            "resolution": "assign",
            "department": "Finance",
            "auto_response": "Assigned to finance team."
        }

    else:
        return {
            "category": "General",
            "summary": "General issue",
            "severity": "Medium",
            "resolution": "assign",
            "department": "Support",
            "auto_response": "Assigned to support team."
        }