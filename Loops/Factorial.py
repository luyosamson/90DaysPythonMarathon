#Programm for a factorial using loops

num=int(input("Enter the number "))

if num<0:
    print("The factorial of a number less than 0 is undefined")
elif num==0 or num==1:
    print("The factorial of 0 and 1 is 1")

elif num>1:
    result = 1
    for i in range(2,num+1):
        
        result*=i
    print(f"The factorial of {num} is ",result)