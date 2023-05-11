    # Python try with else clause
# In some situations, we might want to run a certain
# block of code if the code block inside try runs without any errors.

# For these cases, you can use the optional else keyword with the try statement.


#Program to print reciprical of even numbers

num=int(input("Enter a number "))

if num%2!=0:
    print("Not an even number")
else:
    reciprical=1/num
    print("Reciprical of " +str(num)+ " is",str(reciprical))

try:
    num=int(input("Enter a number "))
    assert num%2==0
except:
    print("Not an even number")
else:
    reciprical=1/num
    print(reciprical)