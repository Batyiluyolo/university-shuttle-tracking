
# tests/test_builder.py

import unittest
from creational_patterns.builder import TripBuilder
from src.trip import Trip

class TestTripBuilder(unittest.TestCase):
    def test_build_trip(self):
        builder = TripBuilder()
        trip = (builder
                .set_trip_id("T123")
                .set_start_time("2025-04-30 08:00")
                .set_end_time("2025-04-30 09:00")
                .set_route_id("R101")
                .set_shuttle_id("SH456")
                .build())

        self.assertIsInstance(trip, Trip)
        self.assertEqual(trip.trip_id, "T123")
        self.assertEqual(trip.status, "Planned")
        self.assertEqual(trip.start_time, "2025-04-30 08:00")
        self.assertEqual(trip.end_time, "2025-04-30 09:00")
        self.assertEqual(trip.route_id, "R101")
        self.assertEqual(trip.shuttle_id, "SH456")

if __name__ == "__main__":
    unittest.main()
