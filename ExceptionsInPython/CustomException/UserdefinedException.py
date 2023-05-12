# Defining Custom Exceptions
# In Python, we can define custom exceptions by creating a 
# new class that is derived from the built-in Exception class .

# Here, CustomError is a user-defined error which inherits from the Exception class .


# class CustomError(Exception):
#     ...
#     pass


# try:
#    ...

# except CustomError:
#     ...

class InvalidAgeException(Exception):
    pass

number=18

try:
    age=int(input("Enter your age "))
    if age<number:
        raise InvalidAgeException
    else:
        print("Eligible to vote")

except InvalidAgeException:
    print("Cannot vote,InvalidAgeException ocurr")
