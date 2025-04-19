
# creational_patterns/builder.py

from src.trip import Trip

class TripBuilder:
    def __init__(self):
        self.trip_id = None
        self.status = "Planned"
        self.start_time = None
        self.end_time = None
        self.route_id = None
        self.shuttle_id = None

    def set_trip_id(self, trip_id):
        self.trip_id = trip_id
        return self

    def set_start_time(self, start_time):
        self.start_time = start_time
        return self

    def set_end_time(self, end_time):
        self.end_time = end_time
        return self

    def set_route_id(self, route_id):
        self.route_id = route_id
        return self

    def set_shuttle_id(self, shuttle_id):
        self.shuttle_id = shuttle_id
        return self

    def build(self):
        return Trip(
            trip_id=self.trip_id,
            status=self.status,
            start_time=self.start_time,
            end_time=self.end_time,
            route_id=self.route_id,
            shuttle_id=self.shuttle_id
        )
