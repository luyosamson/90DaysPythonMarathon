def fibonacci(n):
    a,b=0,1
    print("Fibonacci series:")
    print(a)

    if n>1:
        print(b)
    
    #Generate the subsequent numbers in series

    for _ in range(1,n):
        next_number=a+b
        print(next_number)
        # a,b=b,next_number
        temp=a #Not going to be used
        a=b
        b=next_number
         
fibonacci(5)