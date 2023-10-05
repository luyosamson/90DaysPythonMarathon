def function(x):
    #Take a global variable
    y=3.142
    z=3*x+1.618*y
    print(f'If you make the above operation with  {x} the result will be  {z}')
    return z
with_golden_ratio=function(2)
print(with_golden_ratio)