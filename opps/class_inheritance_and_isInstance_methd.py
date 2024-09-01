# demostrate the us of isinstance() to check if my_tesla is an instance of car and electric car.
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
    
Electric_c = Electric_Car("Tesla","Small s","598kMH")
print(isinstance(Electric_c,Car))
print(isinstance(Electric_c,Electric_Car))
# print(Electric_c.get_brand())