#Based on scope,we can clasify python variable into three,
        #Local,global and non-local

        #Local variables are declared within a functions,
        #they cant be accessed outside the function

            # name='Hello!Samson' #This is a global variable,it can be accessed outside  greet()
            # def greet():
            #     hello="Good Morning" #This  is a local function

            #     print("Samson,",hello)

            # greet()
            # print(name)  


# Python Nonlocal Variables
# In Python, nonlocal variables are used in nested functions whose local 
# scope is not defined. This means that the variable can be neither in 
# the local nor the global scope.
# We use the nonlocal keyword to create nonlocal variables

pi=5

def mycalc(num):
    
    message = "This a non local variable"

    def mult():
     
     nonlocal message
       
    print("Number 2",message)


    mult()
    
    result=pi+num
    return result

result=mycalc(7)
print(result)
