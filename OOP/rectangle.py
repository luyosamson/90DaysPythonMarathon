# Design a class called "Rectangle" that represents a rectangle object.
#  Include attributes for length and width. Implement methods to calculate the
#   perimeter and area of the rectangle

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        peri=2*self.length+2*self.width
        return peri
    def area(self):
        area=self.length*self.width
        return area
    def display_infor(self):
        perim=self.perimeter()
        areaa=self.area()
        print(f"Length of the Rectangle is {self.length}")
        print(f"Width of the Rectangle is {self.width}")
        # print(f"The perimeter is {perim} and area is {areaa}")

rect1=Rectangle(20,20)
rect1.display_infor()
p=rect1.perimeter()
print(p)
a=rect1.area()
print(a)



