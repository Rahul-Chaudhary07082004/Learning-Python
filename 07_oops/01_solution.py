# Basic class and object
# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model): # for context => python - self / js - this and python - __init__ / js - constructor 
        self.brand = brand
        self.model = model

my_car = Car("Tata", "Safari")
print(my_car.brand)
print(my_car.model)