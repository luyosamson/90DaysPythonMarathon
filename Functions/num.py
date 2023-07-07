def num(num1):
    def incremented_num(num1):
        num1=num1+1
        return num1
  
    num2=incremented_num(num1)
    print(num1,'------>',num2)
num(29)
