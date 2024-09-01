# add a method to the car class that displays the full name of the car(brand and model). 
class Car:
    def __init__(self,brand,moedel):
        self.brand = brand
        self.model = moedel

    def full_name(self):
        return f"{self.brand} {self.model}"

obj = Car("toyota","audi")
print(obj.full_name())
