# Write a program that takes two integers as input and 
# checks if the first number is divisible by the second number.
num1=int(input("Enter number 1\t"))
num2=int(input("Enter number 2\t"))

if num1%num2==0:
    print("Num1 is perfectly divisible by Num2")
else:
    print("The two numbers are not divisible")