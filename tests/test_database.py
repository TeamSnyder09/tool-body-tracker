"""Unit tests for database operations"""

import unittest
import os
import tempfile
from src.database import ToolTrackerDB

class TestToolTrackerDB(unittest.TestCase):
    """Test cases for ToolTrackerDB"""
    
    def setUp(self):
        """Set up test database"""
        self.test_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.test_db.close()
        self.db = ToolTrackerDB(self.test_db.name)
    
    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.test_db.name):
            os.remove(self.test_db.name)
    
    def test_add_machine(self):
        """Test adding a machine"""
        machine_id = self.db.add_machine("TestMachine")
        self.assertIsNotNone(machine_id)
        
        # Verify we can retrieve it
        retrieved_id = self.db.get_machine_id("TestMachine")
        self.assertEqual(machine_id, retrieved_id)
    
    def test_add_duplicate_machine(self):
        """Test adding duplicate machine raises error"""
        self.db.add_machine("TestMachine")
        with self.assertRaises(ValueError):
            self.db.add_machine("TestMachine")
    
    def test_add_tool(self):
        """Test adding a tool"""
        tool_id = self.db.add_tool("TestTool", "TypeA")
        self.assertIsNotNone(tool_id)
        
        retrieved_id = self.db.get_tool_id("TestTool")
        self.assertEqual(tool_id, retrieved_id)
    
    def test_add_installation(self):
        """Test adding an installation record"""
        record_id = self.db.add_installation(
            machine_name="Machine1",
            tool_name="Tool1",
            installed_date="2025-12-05"
        )
        self.assertIsNotNone(record_id)
        
        records = self.db.get_all_installations()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]['machine'], "Machine1")
        self.assertEqual(records[0]['tool'], "Tool1")
    
    def test_get_installations_by_machine(self):
        """Test filtering by machine"""
        self.db.add_installation("Machine1", "Tool1", "2025-12-05")
        self.db.add_installation("Machine1", "Tool2", "2025-12-06")
        self.db.add_installation("Machine2", "Tool1", "2025-12-05")
        
        records = self.db.get_installations_by_machine("Machine1")
        self.assertEqual(len(records), 2)
    
    def test_search_installations(self):
        """Test searching installations"""
        self.db.add_installation("Machine1", "Tool1", "2025-12-05")
        self.db.add_installation("Machine2", "Tool1", "2025-12-06")
        
        records = self.db.search_installations("Machine1")
        self.assertEqual(len(records), 1)

if __name__ == '__main__':
    unittest.main()
