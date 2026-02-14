from typing import Dict, List
from .models import Asset, Vulnerability, Playbook, Incident, SecretItem

class InMemoryStore:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}
        self.vulns: Dict[str, Vulnerability] = {}
        self.playbooks: Dict[str, Playbook] = {}
        self.incidents: Dict[str, Incident] = {}
        self.secrets: Dict[str, SecretItem] = {}

store = InMemoryStore()

# helper functions
def add_asset(asset: Asset):
    store.assets[asset.id] = asset
    return asset

def list_assets():
    return list(store.assets.values())

def get_asset(aid: str):
    return store.assets.get(aid)

# vulnerabilities

def add_vuln(v: Vulnerability):
    store.vulns[v.id] = v
    return v

def list_vulns():
    return list(store.vulns.values())

# playbooks

def add_playbook(p: Playbook):
    store.playbooks[p.id] = p
    return p

def list_playbooks():
    return list(store.playbooks.values())

# incidents

def add_incident(i: Incident):
    store.incidents[i.id] = i
    return i

def list_incidents():
    return list(store.incidents.values())

# secrets (in-memory demo)

def add_secret(s: SecretItem):
    store.secrets[s.id] = s
    return s

def list_secrets():
    return list(store.secrets.values())
