class Student:
    def pass_status(self):
        if self.marks >= 50:
            return True
        else:
            return False
#Init method is used to initialize name and marks variales
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


student1 = Student("Harry",25)
print(student1.name)
print(student1.marks)
did_pass=student1.pass_status()
print(did_pass)




