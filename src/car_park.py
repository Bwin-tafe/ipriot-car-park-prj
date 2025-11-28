from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, capacity = 100, plates = None, displays = None, location = "Unknown", ):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = []

    def __str__(self):
        return f"Car park at {self.location} with {self.capacity} bays"

    def register(self, component):
        if isinstance(component, Display):
            self.displays.append(component)
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            raise TypeError("Object must be of type Display or Sensor")

    def add_car(self):
        pass

    def remove_car(self):
        pass

    def update_displays(self):
        pass