# repositories/future/file_trip_repository.py

from repositories.trip_repository import TripRepository
from src.trip import Trip

class FileSystemTripRepository(TripRepository):
    def save(self, trip: Trip) -> None:
        raise NotImplementedError("This will save the trip to a file in the future.")

    def find_by_id(self, trip_id: str) -> Trip:
        raise NotImplementedError("This will retrieve the trip from a file in the future.")

    def find_all(self) -> list[Trip]:
        raise NotImplementedError("This will list all trips stored in files.")

    def delete(self, trip: Trip) -> None:
        raise NotImplementedError("This will delete a trip from the file system.")
