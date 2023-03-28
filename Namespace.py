# Scope and namespace in Python

global_variable=90

def outer_fxn():
    outer_var=9
    
def inner_fxn():
    inner_variable=90

    print(inner_variable)
    

    inner_fxn()

    print(global_variable)

    outer_fxn()

