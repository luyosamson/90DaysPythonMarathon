

        # Access and Modify Python Global Variable
c=10
def x():
 
 #Use global keyword to modify the global variable inside a function
 global c
#  c=10

 #Increament c
 c=c+2
 print(c)

x()

            # Global in Nested Functions
def outer_fnx():
 x=100

def inner_fxn():
        global x
        x=200
print("Before calling inner function",x)

inner_fxn()

print("After calling inner function",x)

outer_fnx()

print("After calling outer function",x)