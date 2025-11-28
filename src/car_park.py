from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location = "Unknown", capacity = 0, plates = None, displays = None, log_file = Path("log.txt"), config_file = Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file

    def __str__(self):
        return f"Car park at {self.location} with {self.capacity} bays"

    def register(self, component):
        if isinstance(component, Display):
            self.displays.append(component)
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            raise TypeError("Object must be of type Display or Sensor")

    def add_car(self, plate : str):
        self.plates.append(plate)
        self.update_displays()
        self.__log_car_activity(plate,"entered")

    def remove_car(self, plate : str):
        self.plates.remove(plate)
        self.update_displays()
        self.__log_car_activity(plate, "exited")

    def update_displays(self):
        data = {"available_bays" : self.available_bays, "temperature" : 25}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        available_bays = self.capacity - len(self.plates)
        if available_bays < 0:
            return 0
        elif available_bays >= 0:
            return available_bays

    def __log_car_activity(self,plate,action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
       with open(self.config_file, "w") as f:
          json.dump({"location": self.location,
                     "capacity": self.capacity,
                     "log_file": str(self.log_file)}, f)

# ... inside the CarPark class
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
       config_file = config_file if isinstance(config_file, Path) else Path(config_file)
       with config_file.open() as f:
          config = json.load(f)
       return cls(config["location"], config["capacity"], log_file=config["log_file"])