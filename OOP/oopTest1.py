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
        return self.length*self.width
  
    def calculate_perimeter(self):
        return 2*(self.length+self.width)
 

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius
     

    def calculate_perimeter(self):
        return 2*math.pi*self.radius
      

r1=Rectangle(7,5)
area=r1.calculate_area()
perimeter=r1.calculate_perimeter()

print(f"The area of the rectangle is ,{area} and the perimeter is , {perimeter}")

c1=Circle(5)
c1.calculate_perimeter()
