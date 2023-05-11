# Python try ...finally
# In Python, the finally block is always executed no matter whether there is an exception or not .

# The finally block is optional. And, for each try block, there can be only one finally block.
try:
    denominator=0
    numerator=10
    result=numerator/denominator
    print(result)

except:
    print("ERROR:Denominator cannot be 0")

finally:
    print("This is the final block")