from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
app = FastAPI()
load_dotenv()
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

    prompt = f"""
    You are an AI ticket classifier.

    Analyze this ticket and return JSON:

    {{
      "category": "",
      "summary": "",
      "severity": "",
      "resolution": "",
      "department": "",
      "sentiment": "",
      "confidence": "",
      "estimated_time": ""
    }}

    Ticket: {ticket.text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        ai_output = response.choices[0].message.content

        return {"ai_result": ai_output}

    except:
        # fallback if AI fails
        return {
            "category": "General",
            "summary": "Fallback response",
            "severity": "Medium",
            "department": "Support",
            "resolution": "assign"
        }