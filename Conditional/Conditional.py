marks=int(input("Enter your marks\n"))

if marks>80:
    print("A")

elif marks>70:
    print("B")
elif marks>60:
    print("C")
elif marks>50:
    print("D")
else:
    print("Retake")

for i in range(10,20):
         print(i)

name=["Mary","Wambui","Kelvin","Kevo","Maryann"]
for x in range(len(name)):
        print(x,name[x])