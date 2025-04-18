
# src/schedule.py

class Schedule:
    def __init__(self, schedule_id, date, time_slot, trip_id):
        self.schedule_id = schedule_id
        self.date = date
        self.time_slot = time_slot
        self.trip_id = trip_id

    def create_schedule(self):
        print(f"Schedule {self.schedule_id} created for trip {self.trip_id}.")

    def update_schedule(self, date=None, time_slot=None):
        if date:
            self.date = date
        if time_slot:
            self.time_slot = time_slot
        print(f"Schedule {self.schedule_id} updated.")

    def archive_schedule(self):
        print(f"Schedule {self.schedule_id} archived.")
