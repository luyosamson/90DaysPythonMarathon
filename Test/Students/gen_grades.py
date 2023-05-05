def grades(aver):
    if aver>=80:
        grade="A"
        return grade
    elif aver>=75:
        grade="A-"
        return grade
    elif aver>=70:
        grade="B+"
        return grade
    elif aver>=65:
        grade="B"
        return grade
    else:
        print("You have failed")
        exit()

    
    