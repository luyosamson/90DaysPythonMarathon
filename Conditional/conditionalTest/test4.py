#Write a Python program that takes a year as input and checks if it is a leap year.
#If it is a leap year, print "Leap year", otherwise print "Not a leap year". 
#(Note: A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.)
date=int(input("Enter a year "))

if date%4==0:
    print("This is a leap year")
else:
    print("This is not a leap year")
    




