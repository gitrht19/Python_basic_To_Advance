# create a car class with attributes like brand and model. then create an instance of this class . 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
new_car = Car("BMW","Audi")
print(new_car.model, new_car.brand)