class CarPark:
    def __init__(self, capacity = 100, plates = None, displays = None, location = "Unknown", ):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at {self.location} with {self.capacity} bays"