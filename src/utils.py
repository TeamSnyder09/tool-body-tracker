"""Utility functions for tool tracking"""

from datetime import datetime
import re

def validate_date(date_string: str) -> bool:
    """Validate date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(time_string: str) -> bool:
    """Validate time format (HH:MM:SS)"""
    try:
        datetime.strptime(time_string, "%H:%M:%S")
        return True
    except ValueError:
        return False

def format_record(record: dict) -> dict:
    """Format record for display"""
    formatted = record.copy()
    if formatted.get("created_at"):
        try:
            dt = datetime.fromisoformat(formatted["created_at"])
            formatted["created_at"] = dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass
    return formatted

def calculate_days_installed(installed_date: str, removal_date: str = None) -> int:
    """Calculate days a tool was installed"""
    try:
        start = datetime.strptime(installed_date, "%Y-%m-%d")
        end = datetime.strptime(removal_date, "%Y-%m-%d") if removal_date else datetime.now()
        return (end - start).days
    except ValueError:
        return 0
