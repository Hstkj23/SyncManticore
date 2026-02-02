# test_syncmanticore.py
"""
Tests for SyncManticore module.
"""

import unittest
from syncmanticore import SyncManticore

class TestSyncManticore(unittest.TestCase):
    """Test cases for SyncManticore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SyncManticore()
        self.assertIsInstance(instance, SyncManticore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SyncManticore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
