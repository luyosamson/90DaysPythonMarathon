class Rectangle:
    length=1
    width=1

    #Method to calculate area
    def area(self):
        result=self.length*self.width
        print("Area is ",result)

rectangle=Rectangle()
rectangle.length=20
rectangle.width=20
rectangle.area()

