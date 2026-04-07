# Synapse AI – Multi-Agent Productivity Assistant

## Overview
Prototype multi-agent AI system demonstrating orchestration between task, calendar, notes, and email agents.

## Features
- Orchestrator + sub-agents
- Demo mode (no API key required)
- FastAPI backend
- Cloud Run deployable

## Run locally
pip install fastapi uvicorn
uvicorn main:app --reload

## Deploy
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/synapse-ai
gcloud run deploy synapse-ai --image gcr.io/YOUR_PROJECT_ID/synapse-ai --allow-unauthenticated
