"""Database management for tool tracking"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Tuple, Optional

DB_PATH = "tool_tracker.db"

class ToolTrackerDB:
    """Database handler for tool installation records"""
    
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create machines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS machines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create tools table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create installation records table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS installations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                machine_id INTEGER NOT NULL,
                tool_id INTEGER NOT NULL,
                installed_date DATE NOT NULL,
                installation_time TIME,
                removal_date DATE,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (machine_id) REFERENCES machines(id),
                FOREIGN KEY (tool_id) REFERENCES tools(id),
                UNIQUE(machine_id, tool_id, installed_date)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_machine(self, name: str) -> int:
        """Add a new machine"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO machines (name) VALUES (?)", (name,))
            conn.commit()
            machine_id = cursor.lastrowid
            return machine_id
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError(f"Machine '{name}' already exists")
        finally:
            conn.close()
    
    def add_tool(self, name: str, tool_type: str = None) -> int:
        """Add a new tool"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO tools (name, type) VALUES (?, ?)",
                (name, tool_type)
            )
            conn.commit()
            tool_id = cursor.lastrowid
            return tool_id
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError(f"Tool '{name}' already exists")
        finally:
            conn.close()
    
    def get_machine_id(self, name: str) -> Optional[int]:
        """Get machine ID by name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM machines WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def get_tool_id(self, name: str) -> Optional[int]:
        """Get tool ID by name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tools WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def add_installation(self, machine_name: str, tool_name: str, 
                        installed_date: str, installation_time: str = None,
                        notes: str = None) -> int:
        """Add an installation record"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get or create machine
        machine_id = self.get_machine_id(machine_name)
        if machine_id is None:
            machine_id = self.add_machine(machine_name)
        
        # Get or create tool
        tool_id = self.get_tool_id(tool_name)
        if tool_id is None:
            tool_id = self.add_tool(tool_name)
        
        try:
            cursor.execute("""
                INSERT INTO installations 
                (machine_id, tool_id, installed_date, installation_time, notes)
                VALUES (?, ?, ?, ?, ?)
            """, (machine_id, tool_id, installed_date, installation_time, notes))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError(f"Installation record already exists for {machine_name} and {tool_name} on {installed_date}")
        finally:
            conn.close()
    
    def get_all_installations(self) -> List[Dict]:
        """Get all installation records"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                m.name as machine, t.name as tool, t.type as tool_type,
                i.installed_date, i.installation_time, i.removal_date,
                i.notes, i.created_at
            FROM installations i
            JOIN machines m ON i.machine_id = m.id
            JOIN tools t ON i.tool_id = t.id
            ORDER BY i.installed_date DESC
        """)
        
        columns = [description[0] for description in cursor.description]
        records = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return records
    
    def get_installations_by_machine(self, machine_name: str) -> List[Dict]:
        """Get installation records for a specific machine"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                m.name as machine, t.name as tool, t.type as tool_type,
                i.installed_date, i.installation_time, i.removal_date,
                i.notes, i.created_at
            FROM installations i
            JOIN machines m ON i.machine_id = m.id
            JOIN tools t ON i.tool_id = t.id
            WHERE m.name = ?
            ORDER BY i.installed_date DESC
        """, (machine_name,))
        
        columns = [description[0] for description in cursor.description]
        records = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return records
    
    def get_installations_by_tool(self, tool_name: str) -> List[Dict]:
        """Get installation records for a specific tool"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                m.name as machine, t.name as tool, t.type as tool_type,
                i.installed_date, i.installation_time, i.removal_date,
                i.notes, i.created_at
            FROM installations i
            JOIN machines m ON i.machine_id = m.id
            JOIN tools t ON i.tool_id = t.id
            WHERE t.name = ?
            ORDER BY i.installed_date DESC
        """, (tool_name,))
        
        columns = [description[0] for description in cursor.description]
        records = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return records
    
    def search_installations(self, query: str) -> List[Dict]:
        """Search installation records by machine or tool name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        search_pattern = f"%{query}%"
        cursor.execute("""
            SELECT 
                m.name as machine, t.name as tool, t.type as tool_type,
                i.installed_date, i.installation_time, i.removal_date,
                i.notes, i.created_at
            FROM installations i
            JOIN machines m ON i.machine_id = m.id
            JOIN tools t ON i.tool_id = t.id
            WHERE m.name LIKE ? OR t.name LIKE ? OR i.notes LIKE ?
            ORDER BY i.installed_date DESC
        """, (search_pattern, search_pattern, search_pattern))
        
        columns = [description[0] for description in cursor.description]
        records = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return records
    
    def get_statistics(self) -> Dict:
        """Get statistics about tool installations"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total records
        cursor.execute("SELECT COUNT(*) FROM installations")
        total_records = cursor.fetchone()[0]
        
        # Total machines
        cursor.execute("SELECT COUNT(*) FROM machines")
        total_machines = cursor.fetchone()[0]
        
        # Total tools
        cursor.execute("SELECT COUNT(*) FROM tools")
        total_tools = cursor.fetchone()[0]
        
        # Tools per machine
        cursor.execute("""
            SELECT m.name, COUNT(*) as tool_count
            FROM installations i
            JOIN machines m ON i.machine_id = m.id
            GROUP BY m.name
            ORDER BY tool_count DESC
        """)
        tools_per_machine = {row[0]: row[1] for row in cursor.fetchall()}
        
        conn.close()
        
        return {
            "total_records": total_records,
            "total_machines": total_machines,
            "total_tools": total_tools,
            "tools_per_machine": tools_per_machine
        }
