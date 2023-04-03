#Tuples are immutable
#Enclosed in () brackets

fruits=('Apple','Guava','Banana','Mangoes','Oranges')
print(fruits)

print(fruits[-2])
#Repeat
print(('Apple',)*4)

#In appending an item to a tuple,you first change a tuple to a list

# y=list(fruits)
# y.append("Grapes")
# print(tuple(y))

fruits2=('Avocado',)
fruits+=fruits2
print(fruits)

for n in  fruits:
    print(n)