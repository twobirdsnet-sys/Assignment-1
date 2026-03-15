from abc import ABC, abstractmethod
import json


# -----------------------------
# Sensor System (Modular Design)
# -----------------------------

class Sensor:
    def read(self):
        pass


class Lidar(Sensor):
    def read(self):
        return "Scanning environment using LIDAR"


class GPS(Sensor):
    def read(self):
        return "Obtaining coordinates from GPS"


# -----------------------------
# Abstract Base Class: Drone
# -----------------------------

class Drone(ABC):

    def __init__(self, drone_id, battery_level):
        self.drone_id = drone_id
        self.__battery_level = battery_level # private variable
        self._internal_temperature = 30 # protected variable
        self.sensors = []

    # Read-only property for battery
    @property
    def battery_level(self):
        return self.__battery_level

    # Concrete method
    def update_battery(self, consumption):
        self.__battery_level -= consumption

        if self.__battery_level < 0:
            self.__battery_level = 0

    # Add sensors dynamically
    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    # Abstract navigation method
    @abstractmethod
    def Maps(self, destination):
        pass


# -----------------------------
# DeliveryDrone Subclass
# -----------------------------

class DeliveryDrone(Drone):

    # Override navigation method
    def Maps(self, destination):

        print(f"Drone {self.drone_id} navigating to {destination}")

        # Use sensors
        for sensor in self.sensors:
            print(sensor.read())

        # Battery consumption
        self.update_battery(10)

    # -----------------------------
    # Save Drone State to JSON
    # -----------------------------
    def save_state(self, filename):

        data = {
            "drone_id": self.drone_id,
            "battery_level": self.battery_level,
            "temperature": self._internal_temperature,
            "sensors": [type(sensor).__name__ for sensor in self.sensors]
        }

        with open(filename, "w") as file:
            json.dump(data, file)

        print("Drone state saved successfully.")

    # -----------------------------
    # Reboot Drone from JSON
    # -----------------------------
    @classmethod
    def reboot(cls, filename):

        with open(filename, "r") as file:
            data = json.load(file)

        drone = cls(data["drone_id"], data["battery_level"])
        drone._internal_temperature = data["temperature"]

        # Recreate sensors
        for sensor_name in data["sensors"]:

            if sensor_name == "GPS":
                drone.add_sensor(GPS())

            elif sensor_name == "Lidar":
                drone.add_sensor(Lidar())

        print("Drone rebooted from saved state.")

        return drone


# -----------------------------
# Simulation Example
# -----------------------------

# Create a drone
d1 = DeliveryDrone("DR-101", 100)

# Inject sensors dynamically
d1.add_sensor(GPS())
d1.add_sensor(Lidar())

# Navigate to destination
d1.Maps("Warehouse A")

# Save state to file
d1.save_state("drone_state.json")

# Reboot drone from saved file
d2 = DeliveryDrone.reboot("drone_state.json")

print("Rebooted Drone Battery Level:", d2.battery_level)