class Animal:
    def __init__(self, name, legs, origin):
        self.name = name
        self.legs = legs
        self.origin = origin

    def sound(self):
        pass


class Dog(Animal):

    def __init__(self, name, legs, origin):
        super().__init__(name, legs, origin)
        print("Bark")


class Cow(Animal):
    def __init__(self, name, legs, origin):
        super().__init__(name, legs, origin)
        print("Moo")


dog = Dog("Buss", 5, "China")
cow = Cow("Ratego", 9, "Fresian")
cow.sound()
