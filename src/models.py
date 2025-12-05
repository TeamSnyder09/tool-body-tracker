"""Data models for tool tracking"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Machine:
    """Represents a machine"""
    id: int
    name: str
    created_at: datetime

@dataclass
class Tool:
    """Represents a tool"""
    id: int
    name: str
    tool_type: Optional[str]
    created_at: datetime

@dataclass
class Installation:
    """Represents a tool installation record"""
    id: int
    machine_name: str
    tool_name: str
    installed_date: str
    installation_time: Optional[str]
    removal_date: Optional[str]
    notes: Optional[str]
    created_at: datetime
