import pprint
student={
    "name":"Luyo",
    "age":26,
    "school":"Multimedia University of Kenya",
    "county":"Siaya",
    "sex":"Male"
}

parents={
    "name":"Willson Omondi",
    "relationship":"Father",
    "age":66
}

# student['Marital_Status']="Single"
# print(student)

# for value in student.values():
#     print(value)

# for ke in student:
#     print(ke)

# for ite in student.items():
#     print(ite)

# for key,value in student.items():
#     print(f"{key}:{value}")

print(f"My name is {student.get('name')},I am a student from {student.get('school')}")
student.setdefault("Height",56)
print(student)
student.pop("name")
print(student)

pprint.pprint(student)

information={**student,**parents}
print(information)
pprint.pprint(information)
