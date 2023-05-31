even={2,4,6,8,10,12,14,16,18,20}
odd={1,2,3,7,9,11,13,17,19,21,23}


even.add(22)
print(even)

odd.update([27,29,31])
print(odd)

odd.discard(23)
print(odd)

num = odd.union(even)  # OR num=odd | even
print(num)

# intersection or & will return a set with only the elements that are common to all of them.
num2=odd.intersection(even)
print(num2)