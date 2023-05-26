
def variable_scope():
    global name
    name = "This name is available everywhere because is GLOBAL"
    print(name)
    local_v="I am a local VARIABLE"
    print(local_v)
variable_scope()
print(name)