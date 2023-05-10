# In Python, we can change the current working directory 
# by using the chdir() method.

# The new path that we want to change into must be supplied as a
# string to this method. And we can use both the forward-slash / 
# or the backward-slash \ to separate the path elements.


import os
os.chdir('/home/pyramid/Development')
print(os.getcwd())


print(os.listdir())
