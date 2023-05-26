class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Overload operator
    def __lt__(self,other):
        return self.age<other.age
p1=Person("Samson",89)
p2=Person("Luyo",45)

print(p1>p2)