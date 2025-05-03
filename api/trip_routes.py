
# api/trip_routes.py

from fastapi import APIRouter, HTTPException
from services.trip_service import TripService
from repositories.inmemory.inmemory_trip_repository import InMemoryTripRepository
from src.trip import Trip

router = APIRouter()
trip_service = TripService(InMemoryTripRepository())

@router.post("/trips/", response_model=dict)
def create_trip(trip_id: str, status: str, start_time: str, end_time: str, route_id: str, shuttle_id: str):
    trip = trip_service.create_trip(trip_id, status, start_time, end_time, route_id, shuttle_id)
    return trip.__dict__

@router.get("/trips/", response_model=list)
def get_all_trips():
    return [t.__dict__ for t in trip_service.get_all_trips()]

@router.get("/trips/{trip_id}", response_model=dict)
def get_trip_by_id(trip_id: str):
    trip = trip_service.get_trip_by_id(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip.__dict__

@router.delete("/trips/{trip_id}")
def delete_trip(trip_id: str):
    trip = trip_service.get_trip_by_id(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    trip_service.delete_trip(trip_id)
    return {"message": "Trip deleted successfully"}
