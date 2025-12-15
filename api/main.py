"""Minimal FastAPI app for the project."""
from fastapi import FastAPI

app = FastAPI(title="Automated Job Application Agent")


@app.get("/")
async def root():
    return {"status": "ok", "message": "Automated Job Application Agent API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/search")
async def search(q: str = "engineer", location: str = None):
    # Placeholder: return query info — implement actual manager wiring later
    return {"query": q, "location": location, "results": []}
