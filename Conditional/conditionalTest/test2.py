# Write a Python program that takes three numbers as input and
# finds the maximum among them. Print the maximum number.
x=int(input("Enter first number "))
y=int(input("Enter second number "))
z=int(input("Enter third number "))

if x>y and x>z:
    print("First number is the greatest")
elif y>x and y>z:
    print("Second number is the greatest")
else:
    print("Third numberis the greatest")