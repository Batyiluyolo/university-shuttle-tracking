
# creational_patterns/prototype.py

import copy
from src.schedule import Schedule

class SchedulePrototype:
    def __init__(self, prototype: Schedule):
        self.prototype = prototype

    def clone(self):
        return copy.deepcopy(self.prototype)
