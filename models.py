from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4

class Asset(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    ip: Optional[str] = None
    tags: List[str] = []

class Vulnerability(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    asset_id: str
    title: str
    severity: str = "medium"
    description: Optional[str] = None

class Playbook(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    steps: List[str] = []

class Incident(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: Optional[str] = None
    status: str = "open"

class SecretItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    value: str
    description: Optional[str] = None
