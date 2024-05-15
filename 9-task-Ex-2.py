# Task - 09:  Write a real time ex for Single and Multiple inheritance

#Multiple inheritance:

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

class Car(Vehicle, Engine):
    def set_num_doors(self, num_doors):
        self.num_doors = num_doors
    
    def display_car_info(self):
        self.display_info()  # Call the method from Vehicle
        self.display_engine_info()  # Call the method from Engine
        print(f"Number of Doors: {self.num_doors}")

# Create an instance of Car
my_car = Car()

# Manually set the attributes
my_car.set_make("Toyota")
my_car.set_model("Corolla")
my_car.set_engine_type("V6")
my_car.set_num_doors(4)

# Display car information
my_car.display_car_info()
