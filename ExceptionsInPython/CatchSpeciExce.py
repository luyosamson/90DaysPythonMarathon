
# Python try ...except Block
# The try ...except block is used to handle exceptions 
# in Python. Here's the syntax of try ...except block:

        # try:
        #     # code that may cause exception
        # except:
        #     # code to run when exception occurs



try:

    even_num=[2,4,6,8,10]
    print(even_num[6])

except ZeroDivisionError:
    print("Denominator cannot be zero")
except IndexError:
    print("Index out of bound")