
# src/trip.py

class Trip:
    def __init__(self, trip_id, status, start_time, end_time, route_id, shuttle_id):
        self.trip_id = trip_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.route_id = route_id
        self.shuttle_id = shuttle_id

    def begin(self):
        self.status = "In Progress"
        print(f"Trip {self.trip_id} has started.")

    def end(self):
        self.status = "Completed"
        print(f"Trip {self.trip_id} has ended.")

    def cancel(self):
        self.status = "Cancelled"
        print(f"Trip {self.trip_id} has been cancelled.")
