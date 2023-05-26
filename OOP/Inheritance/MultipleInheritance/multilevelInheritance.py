class Parentclass:
    def parent_class(self):
        print("This is the parent class of multilevel inheritance")

class Childclass1(Parentclass):
    def child1_class(self):
        print("This is child class 1")
        super().parent_class()

class Childclass2(Childclass1):
    def child2_class(self):
        print("This is the child class 2")

c2=Childclass2()
c2.child1_class()
c2.child2_class()