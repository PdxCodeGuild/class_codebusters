import time
import random
from more_classes import Vehicle


class Better_Vehicle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.plate = "Code Busters"
        self.stereo = "Bose"
        self.weapons = "YES"
        self.car_phone = True
        self.ejector_seat = True
        self.hydraulics = True
        self.neon_lights = True

    def __repr__(self):
        return str(self.get_year())


new_car = Better_Vehicle("Honda", "Accord", 2000)
print(new_car.plate)
print(new_car.weapons)
print(new_car.get_mileage())
new_car.accelerate(1, 5)
# while new_car.speed:
#     time.sleep(1)
#     new_car.drive()
#     print(f"Mileage: {new_car.get_mileage()}")
#     print(f"{new_car.speed=}")
#     print(f"{new_car.fuel=}")
#     new_car.go_faster()
#     if new_car.get_mileage() > 1000000:
#         new_car.stop()

cars = []
for i in range(100):
    car = Better_Vehicle("Honda", "Civic", random.randint(1990, 2010))
    cars.append(car)


print(cars)


person = {'name': 'Brad'}
dict()
print(person)
