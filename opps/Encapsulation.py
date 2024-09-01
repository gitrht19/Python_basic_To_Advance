# modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it 
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
print(Electric_c.get_brand())