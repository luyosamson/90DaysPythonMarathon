


def find_sqr(num):
    # num=int(input("Enter the number to find it's square\t"))
    sq=num*num
    return sq

square=find_sqr(5)

print("Square",square)

mult=square*2
print("Twice the square",mult)


import math
power=pow(4,2)
print("The power",power)
sqr_root=math.sqrt(49)
print(sqr_root)

for i in range(1,10):
    sqr=find_sqr(i)
    print("The square of",i ,"=",sqr)