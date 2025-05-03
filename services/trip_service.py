
# services/trip_service.py

from repositories.trip_repository import TripRepository
from src.trip import Trip

class TripService:
    def __init__(self, trip_repository: TripRepository):
        self.trip_repository = trip_repository

    def create_trip(self, trip_id: str, status: str, start_time: str, end_time: str, route_id: str, shuttle_id: str) -> Trip:
        # Optional: Add validation or transformation here
        trip = Trip(trip_id, status, start_time, end_time, route_id, shuttle_id)
        self.trip_repository.save(trip)
        return trip

    def get_trip_by_id(self, trip_id: str) -> Trip:
        return self.trip_repository.find_by_id(trip_id)

    def get_all_trips(self) -> list[Trip]:
        return self.trip_repository.find_all()

    def delete_trip(self, trip_id: str) -> None:
        trip = self.trip_repository.find_by_id(trip_id)
        if trip:
            self.trip_repository.delete(trip)
