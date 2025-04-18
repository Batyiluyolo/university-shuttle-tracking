
# src/route.py

class Route:
    def __init__(self, route_id, origin, destination, stops=None):
        self.route_id = route_id
        self.origin = origin
        self.destination = destination
        self.stops = stops if stops else []

    def add_stop(self, stop):
        self.stops.append(stop)
        print(f"Stop '{stop}' added to Route {self.route_id}.")

    def remove_stop(self, stop):
        if stop in self.stops:
            self.stops.remove(stop)
            print(f"Stop '{stop}' removed from Route {self.route_id}.")

    def update_route(self, origin=None, destination=None):
        if origin:
            self.origin = origin
        if destination:
            self.destination = destination
        print(f"Route {self.route_id} updated.")
