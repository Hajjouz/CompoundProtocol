# test_compoundprotocol.py
"""
Tests for CompoundProtocol module.
"""

import unittest
from compoundprotocol import CompoundProtocol

class TestCompoundProtocol(unittest.TestCase):
    """Test cases for CompoundProtocol class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompoundProtocol()
        self.assertIsInstance(instance, CompoundProtocol)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompoundProtocol()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
