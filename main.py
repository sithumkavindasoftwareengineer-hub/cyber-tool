from fastapi import FastAPI, HTTPException
from .models import Asset, Vulnerability, Playbook, Incident, SecretItem
from . import storage
from typing import List

app = FastAPI(title="Cyber Work Tools API")

@app.get("/health")
def health():
    return {"status": "ok"}

# Assets
@app.post("/assets", response_model=Asset)
def create_asset(a: Asset):
    return storage.add_asset(a)

@app.get("/assets", response_model=List[Asset])
def get_assets():
    return storage.list_assets()

# Vulnerabilities
@app.post("/vulns", response_model=Vulnerability)
def create_vuln(v: Vulnerability):
    if not storage.get_asset(v.asset_id):
        raise HTTPException(status_code=400, detail="Asset not found")
    return storage.add_vuln(v)

@app.get("/vulns", response_model=List[Vulnerability])
def get_vulns():
    return storage.list_vulns()

# Playbooks
@app.post("/playbooks", response_model=Playbook)
def create_playbook(p: Playbook):
    return storage.add_playbook(p)

@app.get("/playbooks", response_model=List[Playbook])
def get_playbooks():
    return storage.list_playbooks()

# Incidents
@app.post("/incidents", response_model=Incident)
def create_incident(i: Incident):
    return storage.add_incident(i)

@app.get("/incidents", response_model=List[Incident])
def get_incidents():
    return storage.list_incidents()

# Secrets (demo)
@app.post("/secrets", response_model=SecretItem)
def create_secret(s: SecretItem):
    return storage.add_secret(s)

@app.get("/secrets", response_model=List[SecretItem])
def get_secrets():
    return storage.list_secrets()
