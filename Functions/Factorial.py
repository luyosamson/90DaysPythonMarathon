#Reccursive function is a function that calls itself
#Example of reccursive function

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
num=90

print("The factorial of",num,"Is",factorial(num))