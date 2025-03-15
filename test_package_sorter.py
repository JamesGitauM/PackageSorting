import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard_package(self):
        """Test standard packages (not bulky, not heavy)"""
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")  # Small and light
        self.assertEqual(sort(100, 100, 90, 19.9), "STANDARD")  # Just under limits
        
    def test_bulky_package(self):
        """Test bulky packages"""
        # Bulky by volume (1,000,000 cm³)
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        # Bulky by dimension (≥ 150cm)
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
        
    def test_heavy_package(self):
        """Test heavy packages (≥ 20kg)"""
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        
    def test_rejected_package(self):
        """Test packages that are both bulky and heavy"""
        # Bulky by volume and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        
        # Bulky by dimension and heavy
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
        
    def test_edge_cases(self):
        """Test edge cases"""
        # Exactly at the limits
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")  # At dimension limit and weight limit
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")  # At volume limit but not heavy
        
        # Very small package
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")
        
        # Very large and heavy package
        self.assertEqual(sort(1000, 1000, 1000, 100), "REJECTED")

if __name__ == '__main__':
    unittest.main()
