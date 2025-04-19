
# tests/test_factory_method.py

import unittest
from creational_patterns.factory_method import (
    StandardShuttleCreator,
    MiniShuttleCreator,
    StandardShuttle,
    MiniShuttle
)

class TestFactoryMethod(unittest.TestCase):
    def test_standard_shuttle_creation(self):
        creator = StandardShuttleCreator()
        shuttle = creator.create_shuttle("S001", "CA12345")
        self.assertIsInstance(shuttle, StandardShuttle)
        self.assertEqual(shuttle.capacity, 40)

    def test_mini_shuttle_creation(self):
        creator = MiniShuttleCreator()
        shuttle = creator.create_shuttle("M001", "CA54321")
        self.assertIsInstance(shuttle, MiniShuttle)
        self.assertEqual(shuttle.capacity, 20)

if __name__ == "__main__":
    unittest.main()
