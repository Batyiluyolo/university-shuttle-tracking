

# src/driver.py

from user import User

class Driver(User):
    def __init__(self, user_id, name, email, password, license_number, assigned_shuttle=None):
        super().__init__(user_id, name, email, password, role="Driver")
        self.license_number = license_number
        self.assigned_shuttle = assigned_shuttle

    def update_location(self, location):
        print(f"Driver {self.name} updated location to: {location}")

    def start_trip(self, trip_id):
        print(f"Driver {self.name} started trip {trip_id}.")

    def complete_trip(self, trip_id):
        print(f"Driver {self.name} completed trip {trip_id}.")

