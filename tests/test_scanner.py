import unittest
from app.scanner import IoTScanner

class TestIoTScanner(unittest.TestCase):
    def test_scan_network(self):
        scanner = IoTScanner('192.168.1.0/24')
        results = scanner.scan_network()
        self.assertIsInstance(results, dict)
        # Add more specific assertions based on expected output

if __name__ == '__main__':
    unittest.main()
