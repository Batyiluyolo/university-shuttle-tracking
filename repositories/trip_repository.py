# repositories/trip_repository.py

from repositories.repository import Repository
from src.trip import Trip

class TripRepository(Repository[Trip, str]):
    pass
