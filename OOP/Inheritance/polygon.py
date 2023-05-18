class Polygon:
    def __init__(self,sides):
        self.sides=sides
    def display_info(self):
        print("A polygon is a two dimentional shape with a straight line")
    def get_perimeter(self):
        perimeter=sum(self.sides)
        return perimeter

class Triangle(Polygon):
    
    def display_info(self):
            print("A triangle is a polygon with 3 edges")
            # Polygon.display_info(self)
            super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
            print("A quadrilateral is a polygon with 4 edges")

t1=Triangle([100,100,100])
perimeter=t1.get_perimeter()
print("Perimeter:",perimeter)
t1.display_info()