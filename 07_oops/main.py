class Car:
    total_Car = 0

    def __init__(self, brand, model):
        self.__brand = brand # by applying two underscore (__) , brand attribute becomes private and can only be accessed by the method (get_brand())
        self.__model = model
        Car.total_Car += 1 

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self): # example of polymorphism same method with different behavior  
        return "for car Petrol or Diesel"
    
    @staticmethod
    def general_description():
         return "Cars are the means of transport"

    @property # helps to access methods like an attribute
    def model(self):
         return self.__model

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
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(Car.total_Car)

my_car2 = Car("tata", "nexon")
print(Car.general_description())

print(my_car2.model) # coz of @property model is being used as attribute

class Battery:
     def Battery_info(self):
          return "this is battery"

class Engine:
     def Engine_info(self):
          return "this is engine"

class ElectricCarTwo(Car, Battery, Engine):
     pass

my_new_tesla = ElectricCarTwo("tesla", "model s")
print(my_new_tesla.Battery_info())
print(my_new_tesla.Engine_info())