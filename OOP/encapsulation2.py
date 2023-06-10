class Car:
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    
    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.__model=model
    def self_year(self,year):
        self.__year=year
my_car=Car("Honda","V8",2016)
print(my_car.get_model())
my_car.set_make("Hyundai")
print(my_car.get_make())
