num=int(input("Enter the number to get its multiplication table"))
size=int(input("Enter the size of the multiplication table"))

for i in range(1,size+1):
    print(f'{num} X {i}={num*i}')