# use a property decorator in the car class to make the model Attribute read-only. 
class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return{"petrol or disel"}
    
    def get_brand(self):
        return self.__brand + "!"
    
    @staticmethod
    def general_description():
        return "cars are means of transport"
    
class Electric_Car(Car):
    def __init__(self,brand, __model,battery_size):
        super().__init__(brand,__model)
        self.battery_size = battery_size
    
    def fuel_type():
        return {"electric charge"}
    
    @property
    def model(self):
        return self.__model
    
# Electric_c = Electric_Car("Tesla","Small s","598kMH")
safari = Car("Tata","velono")
# hundai = Car("hundai","Safari")
# nexon = Car("nexon","Safari")
# print(Electric_c.fuel_type())
# print(safari.fuel_type())
# print(Car.total_car)
safari.model = "city"
print(safari.model)