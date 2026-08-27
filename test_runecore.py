# test_runecore.py
"""
Tests for RuneCore module.
"""

import unittest
from runecore import RuneCore

class TestRuneCore(unittest.TestCase):
    """Test cases for RuneCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RuneCore()
        self.assertIsInstance(instance, RuneCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RuneCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
