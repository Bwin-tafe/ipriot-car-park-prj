from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}: Active: {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        """Creates a random car number plate."""
        return 'FAKE-' + format(random.randint(0,999), '03d')

    def detect_vehicle(self):
        """Creates the plate of the car entering and updates the car park list"""
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        """Adds the detected car to the car list."""
        self.car_park.add_car(plate)
        print(f"Incoming Vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        """Removes the detected car from the car list."""
        self.car_park.remove_car(plate)
        print(f"Outgoing Vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """For the purposes of the assessment, chooses a random plate from the plate list to be designated as exiting the car park"""
        return random.choice(self.car_park.plates)