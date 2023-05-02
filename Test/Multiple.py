# Write a program that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number
# and for multiples of five, print "Buzz". For numbers that are 
# multiples of both three and five, print "FizzBuzz".


for n in range(1,100):
    if n%3==0:
        print("Fizz")
    elif n%5==0:
       print("Buzz")
    elif n%3==0 and n%5==0:
        print("FizzBuzz")
    else:
        print(n)
