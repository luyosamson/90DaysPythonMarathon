#Lambda fxn is a sinle line functions

# add=lambda n1,n2 : n1+n2
# print(add(12,80))


#Getting square of numbers
numbers=[4,2,6,89,45]

sqr_numb=[]

sqr=lambda x: x**2

for x in numbers:
    sqr_numb.append(sqr(x))

print(sqr_numb)