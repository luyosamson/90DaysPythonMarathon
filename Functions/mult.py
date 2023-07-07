def num(*args):
    result = 0
    for n in args:
     n+=1
     result.append(n)
    return result
x=num(1,2,3,9)
print(x)



