# create two classes battery and engine, and let the electric car class inherit from both demostrating multiple inheritance. 
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return {"brand"},{"model"}
    
    def get_brand(self):
        return self.__brand + "!"
    
class Electric_Car(Car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
# Electric_c = Electric_Car("Tesla","Small s","598kMH")
# print(Electric_c.get_brand())

class Battery:
    def battery_info(self):
        return "This is battery."

class Engine:
    def Engine_info(self):
        return "This is Engine."

class ElectricCar(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar("Audii","car")
print(my_new_tesla.battery_info())
print(my_new_tesla.Engine_info())