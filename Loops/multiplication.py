#The programm that gets the multiplication number of 
#the entered number upto 15


number = int(input("ENTER THE NUMBER "))
print(f"The number to get its multiplication table is {number}")
# x=int(input("Enter the first range value"))
# y=int(input("Enter the second range value"))


for n in range(1,16):
    print(("%dX%d=%d")%(number,n,number*n))