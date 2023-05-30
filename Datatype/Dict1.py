student={
    "name":"Luyo",
    "age":56,
    "school":"Multimedia University of Kenya",
    "county":"Siaya",
    "sex":"Male"
}

student['Marital_Status']="Single"
print(student)

for value in student.values():
    print(value)

for ke in student:
    print(ke)

for ite in student.items():
    print(ite)

for key,value in student.items():
    print(f"{key}:{value}")