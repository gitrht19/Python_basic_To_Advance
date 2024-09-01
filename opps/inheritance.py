# create an electric car class that inherits from the car class and has an additional attribute battery_siz. 
class Car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    
    def full_name(self):
        return f"{self.model} {self.brand}"
    
class Electronic_Car(Car):
    def __init__(self,model,brand,battery_size):
        super().__init__(model, brand)
        self.battery_size = battery_size
    
obj = Electronic_Car("audi","v590","59KWH")
print(obj.model)
print(obj.full_name())
print(obj.battery_size)