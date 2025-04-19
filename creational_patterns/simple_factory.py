
# creational_patterns/simple_factory.py

from src.student import Student
from src.driver import Driver
from src.user import User

class UserFactory:
    @staticmethod
    def create_user(user_type, user_id, name, email, password, **kwargs):
        if user_type == "student":
            return Student(user_id, name, email, password, kwargs.get("faculty"), kwargs.get("year"))
        elif user_type == "driver":
            return Driver(user_id, name, email, password, kwargs.get("license_number"))
        elif user_type == "admin":
            return User(user_id, name, email, password, role="Admin")
        else:
            raise ValueError(f"Unknown user type: {user_type}")
