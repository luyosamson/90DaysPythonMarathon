class Student:
    def pass_status(self):
        if self.mark>=50:
            return True
        else:
            return False

student1=Student()
#Initializing variables
student1.mark=30
student1.name="Harry Potter"

myStatus=student1.pass_status()
print(myStatus)

student2=Student()
student2.mark=90
student2.name="Luyo Samson"
myStatus=student2.pass_status()
print(myStatus)

