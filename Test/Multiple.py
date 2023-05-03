# Write a program that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number
# and for multiples of five, print "Buzz". For numbers that are 
# multiples of both three and five, print "FizzBuzz".

for n in range(1,21):
    if n%3==0:
     print("Fizz")
    elif n%5==0:
     print("Buzz")
    elif n%3==0 and n%5==0:
     print("FizzBuzz")
    else:
     print(n)

# Write a program that asks the user for their name and age, 
# and then prints a message that says "Hello [name], you are 
# [age] years old!".

name=input("Enter your name\n")
age=int(input("Enter your age\n"))

print("Hello " + name + "! your age is " + str(age) )


# Write a program that asks the user for a number, and then
# checks whether the number is even or odd. Print a message 
# to let the user know whether the number is even or odd.

num=int(input("Enter the number\n"))

if num<0:
  print("Negative number is not allowed")
elif num % 2 == 0:
  print("The number " + str(num) + " is an EVEN number")
elif num % 2 != 0:
  print("The number " + str(num) + " is an ODD number")
else:
  print("The input is invalid")