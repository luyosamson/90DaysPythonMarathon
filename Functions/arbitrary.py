# def func(*args):
#     for i in args:
#         print(i)
# func(1,2,3)
# list_of_arg_values=[1,3,6,9,11]
# func(*list_of_arg_values)

def add(*numbers):
    result=0
    for i in numbers:
        result=result+i
    return result
    
ans=add(1,2,3,4)
print(ans)