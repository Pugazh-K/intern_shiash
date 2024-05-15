# Task - 09:  Write a real time ex for Hybrid inheritance

class Vehicle:
    def set_make(self, make):
        self.make = make
    
    def set_model(self, model):
        self.model = model
    
    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Engine:
    def set_engine_type(self, engine_type):
        self.engine_type = engine_type
    
    def display_engine_info(self):
        print(f"Engine Type: {self.engine_type}")

class ElectricVehicle(Vehicle):
    def set_battery_capacity(self, battery_capacity):
        self.battery_capacity = battery_capacity
    
    def display_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class ElectricCar(ElectricVehicle, Engine):
    def set_num_doors(self, num_doors):
        self.num_doors = num_doors
    
    def display_car_info(self):
        self.display_info()  # From Vehicle
        self.display_engine_info()  # From Engine
        self.display_battery_info()  # From ElectricVehicle
        print(f"Number of Doors: {self.num_doors}")

# Create an instance of ElectricCar
my_electric_car = ElectricCar()

# Manually set the attributes
my_electric_car.set_make("Tesla")
my_electric_car.set_model("Model S")
my_electric_car.set_engine_type("Electric")
my_electric_car.set_battery_capacity(100)
my_electric_car.set_num_doors(4)

# Display car information
my_electric_car.display_car_info()
