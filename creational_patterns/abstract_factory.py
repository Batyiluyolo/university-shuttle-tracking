
# creational_patterns/abstract_factory.py

from abc import ABC, abstractmethod
from src.driver import Driver
from src.shuttle import Shuttle
from src.student import Student

# Abstract Factory
class UserPackageFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def create_resource(self):
        pass

# Concrete Factory for Driver + Shuttle
class DriverPackageFactory(UserPackageFactory):
    def create_user(self):
        return Driver("D101", "James", "james@example.com", "pass123", "LIC999")

    def create_resource(self):
        return Shuttle("SH101", "CA3333", 30)

# Concrete Factory for Student + Access (Route or Schedule)
class StudentPackageFactory(UserPackageFactory):
    def create_user(self):
        return Student("S101", "Luyolo", "luyolo@example.com", "pass123", "Engineering", "3rd")

    def create_resource(self):
        return "Access to Shuttle Route View"

