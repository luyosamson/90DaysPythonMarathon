#Used when we are not aware of
#number of arguments that is going to be passed

# program to find sum of multiple numbers

def find_sum(*numbers):
    result=0
    for n in numbers:
        result=result+n

        print("Number",n,"Sum",result)
    

find_sum(80,90,56,34,1)



