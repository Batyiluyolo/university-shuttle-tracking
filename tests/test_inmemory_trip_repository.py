# tests/test_inmemory_trip_repository.py

import unittest
from repositories.inmemory.inmemory_trip_repository import InMemoryTripRepository
from src.trip import Trip

class TestInMemoryTripRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryTripRepository()
        self.trip = Trip("T001", "Scheduled", "08:00", "09:00", "R001", "SH001")

    def test_save_and_find_by_id(self):
        self.repo.save(self.trip)
        found = self.repo.find_by_id("T001")
        self.assertIsNotNone(found)
        self.assertEqual(found.trip_id, "T001")

    def test_find_all(self):
        self.repo.save(self.trip)
        all_trips = self.repo.find_all()
        self.assertIn(self.trip, all_trips)

    def test_delete(self):
        self.repo.save(self.trip)
        self.repo.delete(self.trip)
        self.assertIsNone(self.repo.find_by_id("T001"))

if __name__ == "__main__":
    unittest.main()
