# Automated Job Application Agent

Small project skeleton for an automated job-application agent.

Structure
- `core/` - core models and abstract adapters
- `adapters/` - website-specific scrapers/adapters (LinkedIn, Indeed, ...)
- `manager/` - `ScrapingManager` to orchestrate scraping
- `agents/` - high-level agents (resume generation, application agent)
- `db/` - database schemas and migrations
- `api/` - FastAPI endpoints
- `llm_tools/` - LangChain / LLM helper utilities
- `tests/` - unit tests
- `examples/` - runnable example scripts

Quick start
1. Create a virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the example or start the API (after implementing adapters):

```powershell
python examples\example_run.py
uvicorn api.main:app --reload
```

License
- Add your preferred license
