#We first open a file,read and finally close

file1=open("test.txt")
content=file1.read()
print(content)
with open("test2.txt",'w') as myfile:
    myfile.write("I am the HERO\t")
    myfile.write("of this city")