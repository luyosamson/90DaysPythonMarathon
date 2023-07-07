def grade(name,subject,points=90):
    if points>70:
        return(f"{name} has passed {subject} with {points} points")
    else:
        return(f"{name} has failed in {subject} by scoring {points} points")
student1=grade("Mary","Mathematics")
print(student1)
    