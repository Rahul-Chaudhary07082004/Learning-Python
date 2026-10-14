class Car:
    def __init__(self, brand, model):
        self.__brand = brand # by applying two underscore (__) , brand attribute becomes private and can only be accessed by the method (get_brand())
        self.model = model 

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self): # example of polymorphism same method with different behavior  
        return "for car Petrol or Diesel"

my_car = Car("Tata", "Safari")
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())


class ElectricCar(Car): # ElectricCar inherit all properties of Car class by adding Car in () like this ElectricCar(Car)
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # example of polymorphism same method with different behavior
            return "for elecric car Electric charge"

my_tesla = ElectricCar("tesla", "Model S", "90kWh")
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)
print(my_tesla.fuel_type())