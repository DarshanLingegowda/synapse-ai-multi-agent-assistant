# 🚀 Synapse AI – Multi-Agent Productivity Assistant

Synapse AI is a multi-agent AI system designed to help users manage tasks, schedules, notes, and emails through a unified conversational interface.

It demonstrates how an orchestrator agent can coordinate multiple specialized agents to complete real-world workflows.

---

## 🧠 Architecture Overview

- **Orchestrator Agent**
  - Understands user intent
  - Routes tasks to appropriate sub-agents

- **Sub-Agents**
  - 📅 Calendar Agent – Handles scheduling and events
  - ✅ Task Agent – Creates and manages tasks
  - 📝 Notes Agent – Stores and retrieves notes
  - 📧 Email Agent – Summarizes and prioritizes emails

---

## ⚙️ Features

- Multi-agent coordination
- Task, calendar, notes, and email management
- Multi-step workflow execution
- Structured responses from agents
- API-based backend (FastAPI)
- Deployed on Google Cloud Run
- No API key required (demo-ready)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Deployment:** Google Cloud Run  
- **Architecture:** Multi-Agent System  

---

## 🌐 Live Demo

👉 https://synapse-ai-104265193628.asia-south1.run.app/

---

## 🎯 Example Workflow

**Input:**
Plan my day

**Output:**
- Task list generated  
- Calendar events scheduled  
- Email summary provided  
- Notes added  

---

## 🧩 How It Works

1. User sends a request
2. Orchestrator interprets intent
3. Relevant agents are triggered
4. Agents return structured outputs
5. Results are combined and displayed

---

## 🚀 Running Locally

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload

**Output:**
- Task list generated  
- Calendar events scheduled  
- Email summary provided  
- Notes added  

---

## 🧩 How It Works

1. User sends a request
2. Orchestrator interprets intent
3. Relevant agents are triggered
4. Agents return structured outputs
5. Results are combined and displayed

---

## 🚀 Running Locally

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
Open browser:

http://127.0.0.1:8000
📦 Deployment

Deployed using Google Cloud Run:

gcloud builds submit --tag gcr.io/<PROJECT-ID>/synapse-ai
gcloud run deploy synapse-ai \
  --image gcr.io/<PROJECT-ID>/synapse-ai \
  --allow-unauthenticated
