# Yes, you can use built-in Python functions with lambda functions. 
# In fact, one of the main benefits of lambda functions is that 
# they can be used as arguments to other functions. 
# Here are some examples of using built-in Python functions with lambda functions:

# Using map() with a lambda function:
numbers=[2,3,6,8,9,12,45]

square=map(lambda x: x**2,numbers)

print(list(square))

# Using filter() with a lambda function:
numbers=[12,4,3,45,67,4,41,42,48,90]

even_num=filter(lambda x:x%2==0,numbers)
print(list(even_num))

# Using reduce() with a lambda function:

from functools import reduce

num=[1,2,3]

sum=reduce(lambda x,y: x*y,num)

print(sum)
