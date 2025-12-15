"""Core data models used across the project."""
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class JobPosting:
    id: Optional[int]
    title: str
    company: Optional[str]
    location: Optional[str]
    url: str
    summary: Optional[str] = None
    posted_date: Optional[str] = None
    raw: Optional[dict] = None

@dataclass
class Resume:
    name: str
    email: str
    phone: Optional[str]
    skills: List[str]
    experience: List[dict]
    education: List[dict]
    summary: Optional[str] = None
