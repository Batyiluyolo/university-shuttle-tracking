

# creational_patterns/factory_method.py

from abc import ABC, abstractmethod
from src.shuttle import Shuttle

# Concrete Shuttle Variants
class StandardShuttle(Shuttle):
    def __init__(self, shuttle_id, plate_number):
        super().__init__(shuttle_id, plate_number, capacity=40, status="Idle")

class MiniShuttle(Shuttle):
    def __init__(self, shuttle_id, plate_number):
        super().__init__(shuttle_id, plate_number, capacity=20, status="Idle")

# Creator Abstract Class
class ShuttleCreator(ABC):
    @abstractmethod
    def create_shuttle(self, shuttle_id, plate_number):
        pass

# Concrete Creators
class StandardShuttleCreator(ShuttleCreator):
    def create_shuttle(self, shuttle_id, plate_number):
        return StandardShuttle(shuttle_id, plate_number)

class MiniShuttleCreator(ShuttleCreator):
    def create_shuttle(self, shuttle_id, plate_number):
        return MiniShuttle(shuttle_id, plate_number)
