from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
def health():
    return {"status": "running"}

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    user_input = data.get("input", "").lower()

    if "plan" in user_input:
        response = {
            "tasks": ["Study AI", "Practice coding", "Review notes"],
            "calendar": ["10 AM Study", "2 PM Practice", "6 PM Review"],
            "email_summary": "2 important emails pending",
            "notes": "Focus on ML basics"
        }
    elif "email" in user_input:
        response = {"email_summary": "3 unread emails, 1 urgent"}
    elif "task" in user_input:
        response = {"tasks": ["Finish project", "Prepare slides"]}
    else:
        response = {"message": "I manage tasks, calendar, notes, and emails."}

    return JSONResponse(content=response)
