
# src/student.py

from user import User

class Student(User):
    def __init__(self, user_id, name, email, password, faculty, year):
        super().__init__(user_id, name, email, password, role="Student")
        self.faculty = faculty
        self.year = year

    def view_schedule(self):
        print(f"{self.name} is viewing their schedule.")

    def track_shuttle(self):
        print(f"{self.name} is tracking a shuttle.")
