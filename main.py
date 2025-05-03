
# main.py

from fastapi import FastAPI
from api.trip_routes import router as trip_router

app = FastAPI(
    title="University Shuttle Tracking API",
    version="1.0.0",
    description="REST API for managing trips in the shuttle tracking system"
)

app.include_router(trip_router)

# To run:
# uvicorn main:app --reload
