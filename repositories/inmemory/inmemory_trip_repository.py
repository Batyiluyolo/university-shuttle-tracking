# repositories/inmemory/inmemory_trip_repository.py

from repositories.trip_repository import TripRepository
from src.trip import Trip

class InMemoryTripRepository(TripRepository):
    def __init__(self):
        self._trips = {}

    def save(self, trip: Trip) -> None:
        self._trips[trip.trip_id] = trip

    def find_by_id(self, trip_id: str) -> Trip:
        return self._trips.get(trip_id)

    def find_all(self) -> list[Trip]:
        return list(self._trips.values())

    def delete(self, trip: Trip) -> None:
        if trip.trip_id in self._trips:
            del self._trips[trip.trip_id]
