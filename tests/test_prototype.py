
# tests/test_prototype.py

import unittest
from creational_patterns.prototype import SchedulePrototype
from src.schedule import Schedule

class TestPrototype(unittest.TestCase):
    def test_schedule_clone(self):
        original = Schedule("S001", "2025-05-01", "08:00-09:00", "T001")
        prototype = SchedulePrototype(original)
        clone = prototype.clone()

        self.assertIsInstance(clone, Schedule)
        self.assertNotEqual(id(original), id(clone))
        self.assertEqual(clone.schedule_id, "S001")
        self.assertEqual(clone.date, "2025-05-01")
        self.assertEqual(clone.time_slot, "08:00-09:00")
        self.assertEqual(clone.trip_id, "T001")

if __name__ == "__main__":
    unittest.main()
