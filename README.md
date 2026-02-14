Cyber Work Tools — minimal scaffold

This repository contains a minimal scaffold for a cyber security tooling suite:
- Backend: FastAPI (Python) providing simple APIs for Asset Inventory, Vulnerability scanning (lightweight), Playbooks/Automation, Incident/Ticketing, and Secrets store (in-memory demo).
- Frontend: React + Vite minimal app that calls the backend.

Quick start (backend):

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```

Quick start (frontend):

```bash
cd frontend
npm install
npm run dev
```

Notes:
- This is a demo scaffold with in-memory storage. For production, add a database, auth, TLS, and secrets vault.
- I can extend features (scanners, playbook engine, integrations). Tell me which to prioritize.
