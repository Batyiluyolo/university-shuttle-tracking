
# repositories/repository_factory.py

from repositories.inmemory.inmemory_trip_repository import InMemoryTripRepository
from repositories.future.file_trip_repository import FileSystemTripRepository
from repositories.trip_repository import TripRepository

def get_trip_repository(storage_type: str) -> TripRepository:
    if storage_type == "memory":
        return InMemoryTripRepository()
    elif storage_type == "file":
        return FileSystemTripRepository()
    else:
        raise ValueError("Unsupported storage type: choose 'memory' or 'file'")
