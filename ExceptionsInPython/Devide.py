# num=7/0
# print(num)


#Print  Python Built-in Exceptions
print(dir(locals()['__builtins__']))

try:
    numerator=10
    denominator=0

    result=numerator/denominator
    print(result)

except:
    print("Error!Denominator cannot be zero")