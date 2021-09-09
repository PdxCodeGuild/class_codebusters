

import time


class Vehicle:
    def __init__(self, make, model, year, wheels=4, color="purple", doors=4, seats=5, engine=4, mileage=0):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.seats = seats
        self.engine = engine
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.speed = 0
        self.fuel = 100

    def print_year(self):
        print(self.__year)

    def get_year(self):
        return self.__year

    def accelerate(self, rate, time):
        """
        rate: Miles per minute
        time: Number of minutes
        """
        self.speed += rate * time
        print(f"vroooomm! I'm going {self.speed}miles per minute!")

    def drive(self):
        self.__mileage += self.speed
        self.__use_fuel()

    def __use_fuel(self):
        self.fuel -= self.speed * .1
        if self.fuel <= 0:
            self.stop()

    def get_mileage(self):
        return self.__mileage

    def stop(self):
        self.speed = 0

    def go_faster(self):
        self.speed *= 2
        print("VRROOOMMM")

    def e_brake(self):
        pass


# car = Vehicle("Toyota", "Supra", 1998, mileage=14000)
# car.accelerate(5, 10)


# while car.speed:
#     time.sleep(1)
#     car.drive()
#     print(f"Mileage: {car.get_mileage()}")
#     print(f"{car.speed=}")
#     print(f"{car.fuel=}")
#     car.go_faster()
#     if car.get_mileage() > 1000000:
#         car.stop()
