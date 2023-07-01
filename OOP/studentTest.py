class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def average_grade(self,grade):
        grade_sum=sum(grade)
        average_grade=grade_sum/len(grade)
        return average_grade
    def update_age(self,new_age):
        self.age=new_age
        return new_age
    def display_information(self):
        print("Student name",self.name)
        print("Student age",self.age)
        print("Student grade",self.grade)

student1=Student("Samson",18,"A")
student1.update_age(78)
grade=(90,87,56,78,95)
average_grade=student1.average_grade(grade)
print("Average grade",average_grade)
student1.display_information()