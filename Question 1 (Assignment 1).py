class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        return f"The vehicle is moving at {self.speed} km/h."


# Subclass 1
class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    # Overriding the move() method
    def move(self):
        return f"The car {self.brand} is driving on the road at {self.speed} km/h."


# Subclass 2
class Bike(Vehicle):
    def __init__(self, brand, speed, type_of_bike):
        super().__init__(brand, speed)
        self.type_of_bike = type_of_bike

    # Overriding the move() method
    def move(self):
        return f"The bike {self.brand} is riding at {self.speed} km/h."


# Creating objects
vehicle = Vehicle("Generic", 50)
car = Car("Toyota", 120, 4)
bike = Bike("Yamaha", 80, "Sport")

# Calling the method
print(vehicle.move())
print(car.move())
print(bike.move())