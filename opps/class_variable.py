# add a class variable to car that keeps track of the number of cra created. 
class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1

    def full_name(self):
        return {"brand"},{"model"}
    
    def fuel_type(self):
        return{"petrol or disel"}
    
    def get_brand(self):
        return self.__brand + "!"
    
class Electric_Car(Car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return {"electric charge"}
    
Electric_c = Electric_Car("Tesla","Small s","598kMH")
safari = Car("Tata","velono")
hundai = Car("hundai","Safari")
nexon = Car("nexon","Safari")
print(Electric_c.fuel_type())
print(safari.fuel_type())
print(Car.total_car)