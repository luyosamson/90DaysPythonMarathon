def age_status(age):
    if age<18:
        # print("You are not allowed to drink whisky")
        return 'You are not allowed to drink whisky'
    elif age>=100:
        # print("It is risky to take whisky at your age")
        return 'It is risky to take whisky at your age'
    else:
        # print("You can enjoy whisky")
        return 'You can enjoy whisky'

    return age
# print(age_status(45))
age=int(input("Enter your age:"))
a=age_status(age)
print(a)