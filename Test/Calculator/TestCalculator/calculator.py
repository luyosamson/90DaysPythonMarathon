# Create a Python module called "calculator.py" that contains the following functions:

# add(a, b): Returns the sum of two numbers.
# subtract(a, b): Returns the difference of two numbers.
# multiply(a, b): Returns the product of two numbers.
# divide(a, b): Returns the quotient of two numbers.


def add(a,b):
    return a+b
def substract(a,b):
    
    return a-b
def multiply(a,b):
 
    return a*b

def divide(a,b):
    
    if a==0 or b==0:
        print("Cannot devide by 0")
    else:
        return a/b
    
# add(1,1)
