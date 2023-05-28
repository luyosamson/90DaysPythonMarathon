# Write a ternary expression that assigns the value "Even" to the variable `result`
# # if the number `num` is even, and "Odd" otherwise.

# Question 2
# # Convert the following if-else statement into a ternary expression:
# if x > y:
#     result = "X is greater"
# else:
#     result = "Y is greater"


# Question 3
# Write a nested ternary expression that assigns the value "A" if the variable `score` is
# greater than or equal to 90, "B" if it's between 80 and 89 (inclusive), "C" if it's between
# 70 and 79 (inclusive), and "D" otherwise.

num=9

result="Even" if num%2==0 else "Odd"

print(result)

x=700
y=90

result="X is greater" if x>y else "Y is greater"
print(result)

score=70

mark="A" if score>=90 else "B" if score>=80 else "C" if score>=70  else "D"
print(mark)

