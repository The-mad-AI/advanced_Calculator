class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self):
        self.fuel -= 10
        return "!Out of Fuel" if self.fuel < 10 else f"Fuel left: {self.fuel} "

    def refuel(self, amount):
        self.fuel += amount
        return f"current fuel : {self.fuel}"


my_car = Car("BMW", 50)
print(my_car.drive())
print(my_car.drive())
print(my_car.refuel(20))
print(my_car.drive())
