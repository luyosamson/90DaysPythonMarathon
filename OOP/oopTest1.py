import math
class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    
class Rectangle(Shape):

    def __init__(self,length,width):
        self.width=width
        self.length=length

    def calculate_area(self):
        rec_area=self.length*self.width
        print("Area of a rectangle: ",rec_area)
    def calculate_perimeter(self):
        rec_perimeter=2*(self.length+self.width)
        print("Perimeter of a rectangle: ",rec_perimeter)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        area=math.pi*self.radius
        print("Area of a circle: ",area)

    def calculate_perimeter(self):
        perimeter=2*math.pi*self.radius
        print("Perimeter of a circle: ",perimeter)