

# src/shuttle.py

class Shuttle:
    def __init__(self, shuttle_id, plate_number, capacity, status="Idle"):
        self.shuttle_id = shuttle_id
        self.plate_number = plate_number
        self.capacity = capacity
        self.status = status
        self.driver = None

    def assign_driver(self, driver):
        self.driver = driver
        print(f"Driver {driver.name} assigned to Shuttle {self.plate_number}.")

    def send_location(self, location):
        print(f"Shuttle {self.plate_number} sent location: {location}")

