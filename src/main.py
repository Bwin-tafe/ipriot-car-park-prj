from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark("Moondalup",100,log_file="moondalup.txt")
car_park.write_config()
car_park.from_config(car_park.config_file)
entry_sensor_1 = EntrySensor(1,
                             car_park,
                             True)
car_park.register(entry_sensor_1)
exit_sensor_1 = ExitSensor(1,
                           car_park,
                           True)
car_park.register(exit_sensor_1)
display_1 = Display(1,
                    "Welcome to Moondalup",
                    True)
car_park.register(display_1)
for x in range(10):
    for sensor in car_park.sensors:
        if isinstance(sensor, EntrySensor):
            sensor.detect_vehicle()
for x in range(2):
    for sensor in car_park.sensors:
        if isinstance(sensor, ExitSensor):
            sensor.detect_vehicle()