# schema.py – Shared Data Structures

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ResearchItem:
    title: str
    content: str
    source: str
    url: str
    date: datetime
    media_urls: List[str] = None
