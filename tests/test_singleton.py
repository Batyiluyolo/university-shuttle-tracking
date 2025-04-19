
# tests/test_singleton.py

import unittest
from creational_patterns.singleton import SystemConfig

class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        config1 = SystemConfig()
        config2 = SystemConfig()

        config1.set_config("version", "1.0")
        self.assertIs(config1, config2)
        self.assertEqual(config2.get_config("version"), "1.0")

if __name__ == "__main__":
    unittest.main()
