class Myclass:
    def __init__(self):

        self._protected_var=10
        self.__protected_var=20


obj1=Myclass()
print(obj1._protected_var)
        